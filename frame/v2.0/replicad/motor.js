const { makeBox, makeCylinder } = replicad;

const unitSize = 8.0;           // lego unit size
const unitHeight = 9.6;         // lego brick height
const holeInnerDiameter = 4.8;  // lego hole inner diameter
const holeOuterDiameter = 6.2;  // lego hole outer diameter

const main = () => {
    // Base
    const length = unitSize * 16;
    const width = unitSize * 12;
    const height = unitHeight;
    
    let part = makeBox(
        [-length/2, -width/2, 0],
        [length/2, width/2, height]
    );
    
    // Cutouts
    // Cutout at (0, unitSize * 4)
    let cutout1 = makeBox(
        [-unitSize * 3, -unitSize * 2, 0],
        [unitSize * 3, unitSize * 2, unitHeight]
    ).translate(0, unitSize * 4, 0);
    part = part.cut(cutout1);
    
    // Cutout at (0, unitSize * -4)
    let cutout2 = makeBox(
        [-unitSize * 2, -unitSize * 2, 0],
        [unitSize * 2, unitSize * 2, unitHeight]
    ).translate(0, unitSize * -4, 0);
    part = part.cut(cutout2);
    
    // Cutout at (unitSize * -6.5, unitSize * 5)
    let cutout3 = makeBox(
        [-unitSize * 1.5, -unitSize * 1, 0],
        [unitSize * 1.5, unitSize * 1, unitHeight]
    ).translate(unitSize * -6.5, unitSize * 5, 0);
    part = part.cut(cutout3);
    
    // Cutout at (unitSize * 6.5, unitSize * 5)
    let cutout4 = makeBox(
        [-unitSize * 1.5, -unitSize * 1, 0],
        [unitSize * 1.5, unitSize * 1, unitHeight]
    ).translate(unitSize * 6.5, unitSize * 5, 0);
    part = part.cut(cutout4);
    
    // Cutout at (unitSize * -6.5, unitSize * -4)
    let cutout5 = makeBox(
        [-unitSize * 1.5, -unitSize * 2, 0],
        [unitSize * 1.5, unitSize * 2, unitHeight]
    ).translate(unitSize * -6.5, unitSize * -4, 0);
    part = part.cut(cutout5);
    
    // Cutout at (unitSize * 6.5, unitSize * -4)
    let cutout6 = makeBox(
        [-unitSize * 1.5, -unitSize * 2, 0],
        [unitSize * 1.5, unitSize * 2, unitHeight]
    ).translate(unitSize * 6.5, unitSize * -4, 0);
    part = part.cut(cutout6);
    
    // Cutout at (unitSize * -7, 0)
    let cutout7 = makeBox(
        [-unitSize * 1, -unitSize * 2, 0],
        [unitSize * 1, unitSize * 2, unitHeight]
    ).translate(unitSize * -7, 0, 0);
    part = part.cut(cutout7);
    
    // Cutout at (unitSize * 7, 0)
    let cutout8 = makeBox(
        [-unitSize * 1, -unitSize * 2, 0],
        [unitSize * 1, unitSize * 2, unitHeight]
    ).translate(unitSize * 7, 0, 0);
    part = part.cut(cutout8);
    
    // Walls
    const wallHeight1 = unitHeight * (2 + 1/3);
    const wallZ1 = unitHeight;
    
    // Wall at (-5.5, 0)
    let wall1 = makeBox(
        [-unitSize * 0.5, -unitSize * 1, 0],
        [unitSize * 0.5, unitSize * 1, wallHeight1]
    ).translate(unitSize * -5.5, 0, wallZ1);
    part = part.fuse(wall1);
    
    // Wall at (5.5, 0)
    let wall2 = makeBox(
        [-unitSize * 0.5, -unitSize * 1, 0],
        [unitSize * 0.5, unitSize * 1, wallHeight1]
    ).translate(unitSize * 5.5, 0, wallZ1);
    part = part.fuse(wall2);
    
    // Wall at (7.5, 3) with height 2*unitHeight
    let wall3 = makeBox(
        [-unitSize * 0.5, -unitSize * 1, 0],
        [unitSize * 0.5, unitSize * 1, unitHeight * 2]
    ).translate(unitSize * 7.5, unitSize * 3, unitHeight);
    part = part.fuse(wall3);
    
    // Wall at (-7.5, 3) with height 2*unitHeight
    let wall4 = makeBox(
        [-unitSize * 0.5, -unitSize * 1, 0],
        [unitSize * 0.5, unitSize * 1, unitHeight * 2]
    ).translate(unitSize * -7.5, unitSize * 3, unitHeight);
    part = part.fuse(wall4);
    
    // Wall at (-3.5, -5)
    let wall5 = makeBox(
        [-unitSize * 1.5, -unitSize * 1, 0],
        [unitSize * 1.5, unitSize * 1, wallHeight1]
    ).translate(unitSize * -3.5, unitSize * -5, wallZ1);
    part = part.fuse(wall5);
    
    // Wall at (3.5, -5)
    let wall6 = makeBox(
        [-unitSize * 1.5, -unitSize * 1, 0],
        [unitSize * 1.5, unitSize * 1, wallHeight1]
    ).translate(unitSize * 3.5, unitSize * -5, wallZ1);
    part = part.fuse(wall6);
    
    // Wall at (-4, 5.5)
    let wall7 = makeBox(
        [-unitSize * 1, -unitSize * 0.5, 0],
        [unitSize * 1, unitSize * 0.5, wallHeight1]
    ).translate(unitSize * -4, unitSize * 5.5, wallZ1);
    part = part.fuse(wall7);
    
    // Wall at (4, 5.5)
    let wall8 = makeBox(
        [-unitSize * 1, -unitSize * 0.5, 0],
        [unitSize * 1, unitSize * 0.5, wallHeight1]
    ).translate(unitSize * 4, unitSize * 5.5, wallZ1);
    part = part.fuse(wall8);
    
    // Motor shaft holes (X-axis cylinders)
    const motorZ = unitHeight / 2 + 12;
    const outerRadius = holeOuterDiameter / 2;
    const innerRadius = holeInnerDiameter / 2 + 0.2;
    
    // Left side motor holes
    let motorHole1 = makeCylinder(outerRadius, 0.8, [0, 0, 0], [0.8, 0, 0])
        .translate(unitSize * -7 - 0.4, unitSize * 3, motorZ);
    part = part.cut(motorHole1);
    
    let motorHole2 = makeCylinder(outerRadius, 0.8, [0, 0, 0], [0.8, 0, 0])
        .translate(unitSize * -8 - 0.4, unitSize * 3, motorZ);
    part = part.cut(motorHole2);
    
    let motorHole3 = makeCylinder(innerRadius, unitSize, [0, 0, 0], [unitSize, 0, 0])
        .translate(unitSize * -8, unitSize * 3, motorZ);
    part = part.cut(motorHole3);
    
    // Right side motor holes
    let motorHole4 = makeCylinder(outerRadius, 0.8, [0, 0, 0], [0.8, 0, 0])
        .translate(unitSize * 8 - 0.4, unitSize * 3, motorZ);
    part = part.cut(motorHole4);
    
    let motorHole5 = makeCylinder(outerRadius, 0.8, [0, 0, 0], [0.8, 0, 0])
        .translate(unitSize * 7 - 0.4, unitSize * 3, motorZ);
    part = part.cut(motorHole5);
    
    let motorHole6 = makeCylinder(innerRadius, unitSize, [0, 0, 0], [unitSize, 0, 0])
        .translate(unitSize * 7, unitSize * 3, motorZ);
    part = part.cut(motorHole6);

    // Wire holes (Y-axis cylinders)
    const wireZ1 = unitHeight * 1.5;
    const wireZ2 = unitHeight * 2.5;
    
    // Left side wire holes
    let wireHole1 = makeCylinder(outerRadius, 0.8, [0, 0, 0], [0, 0.8, 0])
        .translate(unitSize * -2.5, unitSize * -4 - 0.4, wireZ1);
    part = part.cut(wireHole1);

    let wireHole2 = makeCylinder(outerRadius, 0.8, [0, 0, 0], [0, 0.8, 0])
        .translate(unitSize * -2.5, unitSize * -6 - 0.4, wireZ1);
    part = part.cut(wireHole2);
    
    let wireHole3 = makeCylinder(innerRadius, unitSize * 2, [0, 0, 0], [0, unitSize * 2, 0])
        .translate(unitSize * -2.5, unitSize * -6, wireZ1);
    part = part.cut(wireHole3);
    
    let wireHole4 = makeCylinder(outerRadius, 0.8, [0, 0, 0], [0, 0.8, 0])
        .translate(unitSize * -2.5, unitSize * -4 - 0.4, wireZ2);
    part = part.cut(wireHole4);
    
    let wireHole5 = makeCylinder(outerRadius, 0.8, [0, 0, 0], [0, 0.8, 0])
        .translate(unitSize * -2.5, unitSize * -6 - 0.4, wireZ2);
    part = part.cut(wireHole5);
    
    let wireHole6 = makeCylinder(innerRadius, unitSize * 2, [0, 0, 0], [0, unitSize * 2, 0])
        .translate(unitSize * -2.5, unitSize * -6, wireZ2);
    part = part.cut(wireHole6);
    
    // Right side wire holes
    let wireHole7 = makeCylinder(outerRadius, 0.8, [0, 0, 0], [0, 0.8, 0])
        .translate(unitSize * 2.5, unitSize * -4 - 0.4, wireZ1);
    part = part.cut(wireHole7);
    
    let wireHole8 = makeCylinder(outerRadius, 0.8, [0, 0, 0], [0, 0.8, 0])
        .translate(unitSize * 2.5, unitSize * -6 - 0.4, wireZ1);
    part = part.cut(wireHole8);
    
    let wireHole9 = makeCylinder(innerRadius, unitSize * 2, [0, 0, 0], [0, unitSize * 2, 0])
        .translate(unitSize * 2.5, unitSize * -6, wireZ1);
    part = part.cut(wireHole9);
    
    let wireHole10 = makeCylinder(outerRadius, 0.8, [0, 0, 0], [0, 0.8, 0])
        .translate(unitSize * 2.5, unitSize * -4 - 0.4, wireZ2);
    part = part.cut(wireHole10);
    
    let wireHole11 = makeCylinder(outerRadius, 0.8, [0, 0, 0], [0, 0.8, 0])
        .translate(unitSize * 2.5, unitSize * -6 - 0.4, wireZ2);
    part = part.cut(wireHole11);
    
    let wireHole12 = makeCylinder(innerRadius, unitSize * 2, [0, 0, 0], [0, unitSize * 2, 0])
        .translate(unitSize * 2.5, unitSize * -6, wireZ2);
    part = part.cut(wireHole12);
    
    
    
    // Mounting screw holes
    const screwZ = unitHeight * 2;
    const screwHoleHeight = unitHeight * 2;
    const screwRadius = 1.5;
    
    const screwPositions = [
        // Stamina
        [unitSize * 1, unitSize * 1, 0],
        [unitSize * 1, unitSize * -1, 0],
        [unitSize * -1, unitSize * 1, 0],
        [unitSize * -1, unitSize * -1, 0],
        // Top
        [unitSize * -5.5, 0, screwZ],
        [unitSize * 5.5, 0, screwZ],
        [unitSize * -4, unitSize * -5, screwZ],
        [unitSize * 4, unitSize * -5, screwZ],
        [unitSize * -4, unitSize * 5.5, screwZ],
        [unitSize * 4, unitSize * 5.5, screwZ],
    ];
    
    for (const pos of screwPositions) {
        let screwHole = makeCylinder(screwRadius, screwHoleHeight, [0, 0, 0], [0, 0, screwHoleHeight])
            .translate(pos[0], pos[1], pos[2]);
        part = part.cut(screwHole);
    }
    
    
    // Apply fillet to all edges that are parallel to Z-axis
    part = part.fillet(1.5, (e) => e.inDirection('Z'));
    
    return part;
}