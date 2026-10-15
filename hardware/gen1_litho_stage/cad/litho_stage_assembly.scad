// =============================================================================
// DRAM Foundation VN - Open Hardware CAD
// Project: Gen 1 Macroscopic Lithography Linear Stage
// Target: Grassroots Semiconductor Lithography & Wafer Translation
// Sourcing: Standard 2020 Aluminum Profile, MGN12H Rail, NEMA 17, T8 Leadscrew
// Units: Millimeters (mm)
// =============================================================================

$fn = 40;

// Main Dimensions
FRAME_LENGTH = 300;
FRAME_WIDTH  = 180;
RAIL_LENGTH  = 250;
STAGE_SIZE   = 80;
WAFER_DIAM   = 50.8; // 2-inch wafer (50.8 mm)

// Module: 2020 Aluminum Extrusion Bar
module alu_profile_2020(length) {
    color([0.25, 0.25, 0.25])
    difference() {
        cube([20, 20, length], center=false);
        // Center core hole (5mm)
        translate([10, 10, -1]) cylinder(r=2.5, h=length + 2);
        // T-slots on 4 sides
        translate([10, -0.5, length/2]) cube([6, 3, length + 2], center=true);
        translate([10, 20.5, length/2]) cube([6, 3, length + 2], center=true);
        translate([-0.5, 10, length/2]) cube([3, 6, length + 2], center=true);
        translate([20.5, 10, length/2]) cube([3, 6, length + 2], center=true);
    }
}

// Module: NEMA 17 Stepper Motor
module nema17_motor() {
    color([0.2, 0.2, 0.22]) {
        // Body (42.3 x 42.3 x 40mm)
        cube([42.3, 42.3, 40], center=true);
        // Front boss collar
        translate([0, 0, 21]) cylinder(r=11, h=2);
        // Output shaft (5mm dia, 24mm length)
        color([0.8, 0.8, 0.85])
        translate([0, 0, 22]) cylinder(r=2.5, h=24);
    }
}

// Module: MGN12H Linear Rail and Slider Block
module mgn12h_rail(length) {
    // Rail (12mm width, 8mm height)
    color([0.75, 0.75, 0.8])
    cube([12, length, 8], center=true);
    
    // Carriage Block (MGN12H: 45.4mm length, 27mm width, 13mm height)
    color([0.9, 0.2, 0.2])
    translate([0, 0, 5])
    cube([27, 45, 10], center=true);
}

// Module: T8 Leadscrew & Coupler
module t8_leadscrew(length) {
    color([0.85, 0.85, 0.9])
    cylinder(r=4, h=length, center=true);
    
    // Flexible Coupler (19mm dia, 25mm length)
    color([0.3, 0.5, 0.8])
    translate([0, 0, -length/2 + 12])
    cylinder(r=9.5, h=25, center=true);
}

// Module: Wafer Stage Carrier Top Plate (80x80x6mm)
module wafer_carrier_plate() {
    color([0.85, 0.85, 0.85])
    difference() {
        cube([STAGE_SIZE, STAGE_SIZE, 6], center=true);
        // Wafer pocket recess (2-inch wafer, 1.0mm depth)
        translate([0, 0, 2.6])
        cylinder(r=WAFER_DIAM/2, h=2);
        // Vacuum suction / center inspection through-hole
        cylinder(r=3, h=10, center=true);
        // Mounting screw holes for MGN12H block (20x20mm spacing, M3)
        for (dx = [-10, 10]) {
            for (dy = [-10, 10]) {
                translate([dx, dy, 0]) cylinder(r=1.6, h=10, center=true);
            }
        }
    }
    
    // Visual Silicon Wafer (2-inch, Mirror Grey)
    color([0.3, 0.35, 0.4, 0.9])
    translate([0, 0, 3.2])
    cylinder(r=WAFER_DIAM/2 - 0.2, h=0.5);
}

// Complete Full Assembly
module full_litho_stage_assembly() {
    // 1. Base Frame (2020 Extrusions)
    translate([-FRAME_WIDTH/2 + 10, -FRAME_LENGTH/2, -20])
    rotate([-90, 0, 0]) alu_profile_2020(FRAME_LENGTH);
    
    translate([FRAME_WIDTH/2 - 10, -FRAME_LENGTH/2, -20])
    rotate([-90, 0, 0]) alu_profile_2020(FRAME_LENGTH);
    
    translate([-FRAME_WIDTH/2, -FRAME_LENGTH/2, -20])
    rotate([0, 90, 0]) alu_profile_2020(FRAME_WIDTH);
    
    translate([-FRAME_WIDTH/2, FRAME_LENGTH/2 - 20, -20])
    rotate([0, 90, 0]) alu_profile_2020(FRAME_WIDTH);

    // Center Cross-member for rail mounting
    translate([-10, -FRAME_LENGTH/2, -20])
    rotate([-90, 0, 0]) alu_profile_2020(FRAME_LENGTH);

    // 2. MGN12H Rail (Mounted along center)
    translate([0, 0, 4])
    mgn12h_rail(RAIL_LENGTH);

    // 3. T8 Leadscrew (Mounted parallel, offset X = 25mm)
    translate([25, 0, 4])
    rotate([90, 0, 0])
    t8_leadscrew(RAIL_LENGTH);

    // 4. NEMA 17 Motor (Mounted at front end)
    translate([25, -FRAME_LENGTH/2 - 20, 4])
    rotate([90, 0, 0])
    nema17_motor();

    // 5. Wafer Carrier Stage (Riding on carriage)
    translate([0, 20, 14])
    wafer_carrier_plate();
}

full_litho_stage_assembly();
