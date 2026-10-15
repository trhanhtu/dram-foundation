// =============================================================================
// Module: dram_march_c_bist
// Description: Synthesizable March C- Algorithmic Memory Built-In Self-Test (BIST)
// Architecture: 6-Element March C- State Machine (10N complexity)
// Coverage: Stuck-At Faults (SAF), Transition Faults (TF), Coupling Faults (CF),
//           and Address Decoder Faults (AF) across 1T1C DRAM matrix.
//
// Algorithm Specification:
//   M0: { (w0) }           - Initialize entire memory to zero
//   M1: { ^ (r0, w1) }     - Read 0, write 1 (Ascending Address)
//   M2: { ^ (r1, w0) }     - Read 1, write 0 (Ascending Address)
//   M3: { v (r0, w1) }     - Read 0, write 1 (Descending Address)
//   M4: { v (r1, w0) }     - Read 1, write 0 (Descending Address)
//   M5: { (r0) }           - Verify all cells are zero
// =============================================================================

`timescale 1ns / 1ps

module dram_march_c_bist #(
    parameter ADDR_WIDTH = 8,
    parameter DATA_WIDTH = 8
)(
    input  wire                   clk,
    input  wire                   rst_n,
    input  wire                   start,
    
    // DRAM Memory Controller Interface
    output reg  [ADDR_WIDTH-1:0]  mem_addr,
    output reg  [DATA_WIDTH-1:0]  mem_wdata,
    output reg                    mem_we,
    output reg                    mem_re,
    input  wire [DATA_WIDTH-1:0]  mem_rdata,
    
    // BIST Status & Diagnostic Outputs
    output reg                    bist_done,
    output reg                    bist_pass,
    output reg                    bist_fail,
    output reg  [ADDR_WIDTH-1:0]  fail_addr,
    output reg  [DATA_WIDTH-1:0]  fail_expected,
    output reg  [DATA_WIDTH-1:0]  fail_actual,
    output reg  [3:0]             state_debug
);

    localparam MAX_ADDR = (1 << ADDR_WIDTH) - 1;
    localparam PAT_0    = {DATA_WIDTH{1'b0}};
    localparam PAT_1    = {DATA_WIDTH{1'b1}};

    // FSM State Encoding
    localparam ST_IDLE          = 4'd0;
    localparam ST_M0_INIT       = 4'd1;
    localparam ST_M1_READ       = 4'd2;
    localparam ST_M1_WRITE      = 4'd3;
    localparam ST_M2_READ       = 4'd4;
    localparam ST_M2_WRITE      = 4'd5;
    localparam ST_M3_READ       = 4'd6;
    localparam ST_M3_WRITE      = 4'd7;
    localparam ST_M4_READ       = 4'd8;
    localparam ST_M4_WRITE      = 4'd9;
    localparam ST_M5_READ       = 4'd10;
    localparam ST_M5_CHECK      = 4'd11;
    localparam ST_FINISH        = 4'd12;

    reg [3:0] current_state, next_state;
    reg [ADDR_WIDTH-1:0] addr_reg;
    reg error_flag;
    reg [DATA_WIDTH-1:0] exp_data_reg;

    always @(*) state_debug = current_state;

    // State Transition Logic
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            current_state <= ST_IDLE;
        end else begin
            current_state <= next_state;
        end
    end

    // Next State and Control Datapath
    always @(*) begin
        next_state = current_state;
        case (current_state)
            ST_IDLE: begin
                if (start)
                    next_state = ST_M0_INIT;
            end

            // M0: Write 0 to all addresses
            ST_M0_INIT: begin
                if (addr_reg == MAX_ADDR)
                    next_state = ST_M1_READ;
            end

            // M1: Ascending Read 0, Write 1
            ST_M1_READ: begin
                next_state = ST_M1_WRITE;
            end
            ST_M1_WRITE: begin
                if (addr_reg == MAX_ADDR)
                    next_state = ST_M2_READ;
                else
                    next_state = ST_M1_READ;
            end

            // M2: Ascending Read 1, Write 0
            ST_M2_READ: begin
                next_state = ST_M2_WRITE;
            end
            ST_M2_WRITE: begin
                if (addr_reg == MAX_ADDR)
                    next_state = ST_M3_READ;
                else
                    next_state = ST_M2_READ;
            end

            // M3: Descending Read 0, Write 1
            ST_M3_READ: begin
                next_state = ST_M3_WRITE;
            end
            ST_M3_WRITE: begin
                if (addr_reg == 0)
                    next_state = ST_M4_READ;
                else
                    next_state = ST_M3_READ;
            end

            // M4: Descending Read 1, Write 0
            ST_M4_READ: begin
                next_state = ST_M4_WRITE;
            end
            ST_M4_WRITE: begin
                if (addr_reg == 0)
                    next_state = ST_M5_READ;
                else
                    next_state = ST_M4_READ;
            end

            // M5: Read 0 and verify
            ST_M5_READ: begin
                next_state = ST_M5_CHECK;
            end
            ST_M5_CHECK: begin
                if (addr_reg == MAX_ADDR)
                    next_state = ST_FINISH;
                else
                    next_state = ST_M5_READ;
            end

            ST_FINISH: begin
                next_state = ST_IDLE;
            end

            default: next_state = ST_IDLE;
        endcase
    end

    // Address and Interface Generation
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            addr_reg      <= 0;
            mem_addr      <= 0;
            mem_wdata     <= 0;
            mem_we        <= 1'b0;
            mem_re        <= 1'b0;
            bist_done     <= 1'b0;
            bist_pass     <= 1'b0;
            bist_fail     <= 1'b0;
            error_flag    <= 1'b0;
            fail_addr     <= 0;
            fail_expected <= 0;
            fail_actual   <= 0;
            exp_data_reg  <= 0;
        end else begin
            case (current_state)
                ST_IDLE: begin
                    bist_done <= 1'b0;
                    bist_pass <= 1'b0;
                    bist_fail <= 1'b0;
                    error_flag<= 1'b0;
                    mem_we    <= 1'b0;
                    mem_re    <= 1'b0;
                    addr_reg  <= 0;
                end

                // M0: Init all cells to 0
                ST_M0_INIT: begin
                    mem_addr  <= addr_reg;
                    mem_wdata <= PAT_0;
                    mem_we    <= 1'b1;
                    mem_re    <= 1'b0;
                    if (addr_reg == MAX_ADDR)
                        addr_reg <= 0;
                    else
                        addr_reg <= addr_reg + 1'b1;
                end

                // M1: Read 0, then Write 1 (Ascending)
                ST_M1_READ: begin
                    mem_addr     <= addr_reg;
                    mem_we       <= 1'b0;
                    mem_re       <= 1'b1;
                    exp_data_reg <= PAT_0;
                end
                ST_M1_WRITE: begin
                    // Verify read data
                    if (mem_rdata !== exp_data_reg) begin
                        error_flag <= 1'b1;
                        if (!error_flag) begin
                            fail_addr     <= addr_reg;
                            fail_expected <= exp_data_reg;
                            fail_actual   <= mem_rdata;
                        end
                    end
                    // Write 1
                    mem_addr  <= addr_reg;
                    mem_wdata <= PAT_1;
                    mem_we    <= 1'b1;
                    mem_re    <= 1'b0;
                    if (addr_reg == MAX_ADDR)
                        addr_reg <= 0;
                    else
                        addr_reg <= addr_reg + 1'b1;
                end

                // M2: Read 1, then Write 0 (Ascending)
                ST_M2_READ: begin
                    mem_addr     <= addr_reg;
                    mem_we       <= 1'b0;
                    mem_re       <= 1'b1;
                    exp_data_reg <= PAT_1;
                end
                ST_M2_WRITE: begin
                    // Verify read data
                    if (mem_rdata !== exp_data_reg) begin
                        error_flag <= 1'b1;
                        if (!error_flag) begin
                            fail_addr     <= addr_reg;
                            fail_expected <= exp_data_reg;
                            fail_actual   <= mem_rdata;
                        end
                    end
                    // Write 0
                    mem_addr  <= addr_reg;
                    mem_wdata <= PAT_0;
                    mem_we    <= 1'b1;
                    mem_re    <= 1'b0;
                    if (addr_reg == MAX_ADDR)
                        addr_reg <= MAX_ADDR;
                    else
                        addr_reg <= addr_reg + 1'b1;
                end

                // M3: Read 0, then Write 1 (Descending)
                ST_M3_READ: begin
                    mem_addr     <= addr_reg;
                    mem_we       <= 1'b0;
                    mem_re       <= 1'b1;
                    exp_data_reg <= PAT_0;
                end
                ST_M3_WRITE: begin
                    // Verify read data
                    if (mem_rdata !== exp_data_reg) begin
                        error_flag <= 1'b1;
                        if (!error_flag) begin
                            fail_addr     <= addr_reg;
                            fail_expected <= exp_data_reg;
                            fail_actual   <= mem_rdata;
                        end
                    end
                    // Write 1
                    mem_addr  <= addr_reg;
                    mem_wdata <= PAT_1;
                    mem_we    <= 1'b1;
                    mem_re    <= 1'b0;
                    if (addr_reg == 0)
                        addr_reg <= MAX_ADDR;
                    else
                        addr_reg <= addr_reg - 1'b1;
                end

                // M4: Read 1, then Write 0 (Descending)
                ST_M4_READ: begin
                    mem_addr     <= addr_reg;
                    mem_we       <= 1'b0;
                    mem_re       <= 1'b1;
                    exp_data_reg <= PAT_1;
                end
                ST_M4_WRITE: begin
                    // Verify read data
                    if (mem_rdata !== exp_data_reg) begin
                        error_flag <= 1'b1;
                        if (!error_flag) begin
                            fail_addr     <= addr_reg;
                            fail_expected <= exp_data_reg;
                            fail_actual   <= mem_rdata;
                        end
                    end
                    // Write 0
                    mem_addr  <= addr_reg;
                    mem_wdata <= PAT_0;
                    mem_we    <= 1'b1;
                    mem_re    <= 1'b0;
                    if (addr_reg == 0)
                        addr_reg <= 0;
                    else
                        addr_reg <= addr_reg - 1'b1;
                end

                // M5: Read 0 and verify
                ST_M5_READ: begin
                    mem_addr     <= addr_reg;
                    mem_we       <= 1'b0;
                    mem_re       <= 1'b1;
                    exp_data_reg <= PAT_0;
                end
                ST_M5_CHECK: begin
                    mem_we <= 1'b0;
                    mem_re <= 1'b0;
                    if (mem_rdata !== exp_data_reg) begin
                        error_flag <= 1'b1;
                        if (!error_flag) begin
                            fail_addr     <= addr_reg;
                            fail_expected <= exp_data_reg;
                            fail_actual   <= mem_rdata;
                        end
                    end
                    if (addr_reg == MAX_ADDR)
                        addr_reg <= 0;
                    else
                        addr_reg <= addr_reg + 1'b1;
                end

                ST_FINISH: begin
                    mem_we    <= 1'b0;
                    mem_re    <= 1'b0;
                    bist_done <= 1'b1;
                    bist_pass <= ~error_flag;
                    bist_fail <= error_flag;
                end
            endcase
        end
    end

endmodule
