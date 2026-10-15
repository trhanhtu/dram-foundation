// =============================================================================
// DRAM Foundation VN - Open Hardware CAD
// Project: Gen 1 Photoresist Spin Coater Vacuum Chuck & Splash Bowl Assembly
// Target: Uniform Micro-Lithography Resist Coating (Shipley 1813 / SU-8)
// Units: Millimeters (mm)
// =============================================================================

$fn = 60;

CHUCK_DIAM    = 45.0; // Chuck outer diameter
CHUCK_HEIGHT  = 18.0; // Chuck total height
SHAFT_DIAM    = 3.17; // A2212 motor shaft diameter
ORING_OD      = 28.0; // Silicone O-ring outer diameter
ORING_ID      = 24.0; // Silicone O-ring inner diameter
BOWL_DIAM     = 200.0;// Splash bowl diameter
BOWL_HEIGHT   = 100.0;// Splash bowl depth

// Module: Precision Vacuum Chuck (Lathe / 3D Print PETG)
module vacuum_chuck() {
    color([0.85, 0.85, 0.88])
    difference() {
        cylinder(r=CHUCK_DIAM/2, h=CHUCK_HEIGHT);
        
        // 1. Center vacuum suction passage (3mm bore)
        translate([0, 0, -1])
        cylinder(r=1.5, h=CHUCK_HEIGHT + 2);
        
        // 2. Motor shaft mounting hole (3.17mm) at bottom
        translate([0, 0, -1])
        cylinder(r=SHAFT_DIAM/2 + 0.1, h=10);
        
        // 3. Radial vacuum distribution grooves on top surface
        for (a = [0, 45, 90, 135]) {
            rotate([0, 0, a])
            translate([-18, -0.75, CHUCK_HEIGHT - 0.8])
            cube([36, 1.5, 1.0]);
        }
        
        // 4. Circular O-Ring retention channel on top surface
        translate([0, 0, CHUCK_HEIGHT - 1.2])
        difference() {
            cylinder(r=ORING_OD/2, h=2);
            translate([0, 0, -0.5])
            cylinder(r=ORING_ID/2, h=3);
        }
        
        // 5. M3 grub screw hole on side for shaft locking
        translate([0, 0, 5])
        rotate([90, 0, 0])
        cylinder(r=1.5, h=CHUCK_DIAM/2 + 1);
    }

    // Visual Silicone O-Ring (Red)
    color([0.9, 0.1, 0.1, 0.9])
    translate([0, 0, CHUCK_HEIGHT - 0.4])
    difference() {
        cylinder(r=(ORING_OD - 0.5)/2, h=1.2);
        translate([0, 0, -0.5])
        cylinder(r=(ORING_ID + 0.5)/2, h=2.2);
    }
}

// Module: Splash Containment Bowl & Solvent Drain
module splash_containment_bowl() {
    color([0.9, 0.9, 0.95, 0.4]) // Translucent acrylic / polished stainless
    difference() {
        cylinder(r=BOWL_DIAM/2, h=BOWL_HEIGHT);
        
        // Inner hollow cavity
        translate([0, 0, 4])
        cylinder(r=BOWL_DIAM/2 - 4, h=BOWL_HEIGHT + 1);
        
        // Bottom motor pass-through hole
        translate([0, 0, -2])
        cylinder(r=20, h=10);
        
        // Drain spout hole at bottom edge
        translate([BOWL_DIAM/2 - 15, 0, -2])
        cylinder(r=6, h=10);
    }
    
    // Drain pipe fitting
    color([0.2, 0.2, 0.2])
    translate([BOWL_DIAM/2 - 15, 0, -20])
    difference() {
        cylinder(r=7, h=20);
        translate([0, 0, -1]) cylinder(r=5, h=22);
    }
}

// Full Spin Coater Head Assembly
module full_spin_coater_assembly() {
    // Splash containment bowl
    splash_containment_bowl();
    
    // Vacuum Chuck positioned at center inside bowl
    translate([0, 0, 35])
    vacuum_chuck();
    
    // Wafer resting on chuck (2-inch Silicon Mirror Disc)
    color([0.25, 0.28, 0.35, 0.95])
    translate([0, 0, 35 + CHUCK_HEIGHT + 0.2])
    cylinder(r=50.8/2, h=0.5);
}

full_spin_coater_assembly();
