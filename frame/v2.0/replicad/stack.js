const { makeBox, makeCylinder } = replicad;

const unitSize = 8.0;           // lego unit size
const unitHeight = 9.6;         // lego brick height
const holeInnerDiameter = 4.8;  // lego hole inner diameter
const holeOuterDiameter = 6.2;  // lego hole outer diameter

const main = () => {
    // Base
    const length = unitSize * 32;
    const width = unitSize * 8;
    const height = unitHeight;
    
    let part = makeBox(
        [-length/2, -width/2, 0],
        [length/2, width/2, height]
    );
    
    // Cutouts
    // Cutout at (unitSize * -13, unitSize * 3)
    let cutout1 = makeBox(
        [-unitSize * 3, -unitSize * 1, 0],
        [unitSize * 3, unitSize * 1, unitHeight]
    ).translate(unitSize * -13, unitSize * 3, 0);
    part = part.cut(cutout1);
    
    // Cutout at (unitSize * 13, unitSize * 3)
    let cutout2 = makeBox(
        [-unitSize * 3, -unitSize * 1, 0],
        [unitSize * 3, unitSize * 1, unitHeight]
    ).translate(unitSize * 13, unitSize * 3, 0);
    part = part.cut(cutout2);
    
    // Cutout at (unitSize * -13, unitSize * -3)
    let cutout3 = makeBox(
        [-unitSize * 3, -unitSize * 1, 0],
        [unitSize * 3, unitSize * 1, unitHeight]
    ).translate(unitSize * -13, unitSize * -3, 0);
    part = part.cut(cutout3);
    
    // Cutout at (unitSize * 13, unitSize * -3)
    let cutout4 = makeBox(
        [-unitSize * 3, -unitSize * 1, 0],
        [unitSize * 3, unitSize * 1, unitHeight]
    ).translate(unitSize * 13, unitSize * -3, 0);
    part = part.cut(cutout4);
    
    // Cutout at (unitSize * 3.5, 0)
    let cutout5 = makeBox(
        [-unitSize * 3, -unitSize * 2.75, 0],
        [unitSize * 3, unitSize * 2.75, unitHeight]
    ).translate(unitSize * 3.5, 0, 0);
    part = part.cut(cutout5);
    
    // Cutout at (unitSize * -4.5, 0)
    let cutout6 = makeBox(
        [-unitSize * 3, -unitSize * 2.75, 0],
        [unitSize * 3, unitSize * 2.75, unitHeight]
    ).translate(unitSize * -4.5, 0, 0);
    part = part.cut(cutout6);
    
    // Cutout at (0, 0)
    let cutout7 = makeBox(
        [-unitSize * 8.75, -unitSize * 1.5, 0],
        [unitSize * 8.75, unitSize * 1.5, unitHeight]
    ).translate(0, 0, 0);
    part = part.cut(cutout7);
    
    // Top protrusions (boxes fused to the base)
    const protrusionHeight = unitHeight * 1;
    const protrusionZ = 0;
    
    // Protrusions at various positions
    const protrusionPositions = [
        [unitSize * 3.5, unitSize * 4.5],
        [unitSize * 3.5, unitSize * -4.5],
        [unitSize * -3.5, unitSize * 4.5],
        [unitSize * -3.5, unitSize * -4.5],
        [unitSize * 9, unitSize * -4.5],
        [unitSize * 9, unitSize * 4.5],
        [unitSize * -9, unitSize * 4.5],
        [unitSize * -9, unitSize * -4.5],
    ];
    
    for (const pos of protrusionPositions) {
        let protrusion = makeBox(
            [-unitSize * 1, -unitSize * 0.5, 0],
            [unitSize * 1, unitSize * 0.5, protrusionHeight]
        ).translate(pos[0], pos[1], protrusionZ);
        part = part.fuse(protrusion);
    }
    
    // Mounting screw holes (through holes)
    const screwRadius = 1.5;
    const screwHeight = unitHeight;
    
    const screwPositions = [
        // Wheelbase
        [unitSize * 0,    unitSize * 3.5,  0],
        [unitSize * 0,    unitSize * -3.5, 0],
        [unitSize * 7,    unitSize * 3.5,  0],
        [unitSize * 7,    unitSize * -3.5, 0],
        [unitSize * -7,   unitSize * 3.5,  0],
        [unitSize * -7,   unitSize * -3.5, 0],
        [unitSize * -9.5, 0,               0],
        [unitSize * 9.5,  0,               0],
        // Engines
        [unitSize * 12.0,  unitSize * 1,   0],
        [unitSize * 12.0,  unitSize * -1,  0],
        [unitSize * -12.0, unitSize * 1,   0],
        [unitSize * -12.0, unitSize * -1,  0],
        [unitSize * 14.0,  unitSize * 1,   0],
        [unitSize * 14.0,  unitSize * -1,  0],
        [unitSize * -14.0, unitSize * 1,   0],
        [unitSize * -14.0, unitSize * -1,  0],
        // Arduino
        [unitSize * -1, 24.15, 0],
        [unitSize * -1 - 1.2, -24.15, 0],
        [unitSize * -1 + 75, 24.15, 0],
        [unitSize * -1 - 1.2 + 82.6, -24.15, 0],
        // Top
        [unitSize * 3.5,  unitSize * 4.5,  0],
        [unitSize * -3.5, unitSize * 4.5,  0],
        [unitSize * 3.5,  unitSize * -4.5, 0],
        [unitSize * -3.5, unitSize * -4.5, 0],
        [unitSize * 9,    unitSize * 4.5,  0],
        [unitSize * -9,   unitSize * 4.5,  0],
        [unitSize * 9,    unitSize * -4.5, 0],
        [unitSize * -9,   unitSize * -4.5, 0],
    ];
    
    for (const pos of screwPositions) {
        let screwHole = makeCylinder(screwRadius, screwHeight, [0, 0, 0], [0, 0, screwHeight])
            .translate(pos[0], pos[1], pos[2]);
        part = part.cut(screwHole);
    }
    
    // Counterbore holes (recessed areas for screw heads)
    const counterboreRadius = 3;
    const counterboreHeight = 3;
    const counterboreZ = unitHeight - 3;
    
    const counterborePositions = [
        // Wheelbase
        [unitSize * 0,    unitSize * 3.5,  counterboreZ],
        [unitSize * 0,    unitSize * -3.5, counterboreZ],
        [unitSize * 7,    unitSize * 3.5,  counterboreZ],
        [unitSize * 7,    unitSize * -3.5, counterboreZ],
        [unitSize * -7,   unitSize * 3.5,  counterboreZ],
        [unitSize * -7,   unitSize * -3.5, counterboreZ],
        [unitSize * -9.5, 0,               counterboreZ],
        [unitSize * 9.5,  0,               counterboreZ],
    ];
    
    for (const pos of counterborePositions) {
        let counterbore = makeCylinder(counterboreRadius, counterboreHeight, [0, 0, 0], [0, 0, counterboreHeight])
            .translate(pos[0], pos[1], pos[2]);
        part = part.cut(counterbore);
    }
    
    // Apply fillet to all edges that are parallel to Z-axis
    part = part.fillet(2, (e) => e.inDirection('Z'));
    
    return part;
}