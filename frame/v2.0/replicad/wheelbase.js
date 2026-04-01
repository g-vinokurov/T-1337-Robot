const { makeBox, makeCylinder } = replicad;

const unitSize = 8.0;           // lego unit size
const unitHeight = 9.6;         // lego brick height
const holeInnerDiameter = 4.8;  // lego hole inner diameter
const holeOuterDiameter = 6.2;  // lego hole outer diameter

const main = () => {
    // Base
    const length = unitSize * 22;
    const width = unitSize * 16;
    const height = unitHeight;
    
    let part = makeBox(
        [-length/2, -width/2, 0],
        [length/2, width/2, height]
    );
    
    // Cutouts
    // Cutout at left side
    let cutout1 = makeBox(
        [-unitSize * 1.5, -unitSize * 7, 0],
        [unitSize * 1.5, unitSize * 7, unitHeight]
    ).translate(unitSize * -11 + unitSize * 1.5, 0, 0);
    part = part.cut(cutout1);
    
    // Cutout at right side
    let cutout2 = makeBox(
        [-unitSize * 1.5, -unitSize * 7, 0],
        [unitSize * 1.5, unitSize * 7, unitHeight]
    ).translate(unitSize * 11 - unitSize * 1.5, 0, 0);
    part = part.cut(cutout2);
    
    // Cutout at left-center
    let cutout3 = makeBox(
        [-unitSize * 2.5, -unitSize * 7, 0],
        [unitSize * 2.5, unitSize * 7, unitHeight]
    ).translate(unitSize * -3.5, 0, 0);
    part = part.cut(cutout3);
    
    // Cutout at right-center
    let cutout4 = makeBox(
        [-unitSize * 2.5, -unitSize * 7, 0],
        [unitSize * 2.5, unitSize * 7, unitHeight]
    ).translate(unitSize * 3.5, 0, 0);
    part = part.cut(cutout4);
    
    // Wheel holes (side 1 - top side)
    const wheelZ = unitHeight / 2 + 0.8;
    const outerRadius = holeOuterDiameter / 2;
    const innerRadius = holeInnerDiameter / 2 + 0.2;
    
    for (let i = 1; i <= 21; i++) {
        // Skip certain positions
        if ([3, 4, 5, 10, 11, 12, 17, 18, 19].includes(i)) {
            continue;
        }
        
        const xPos = unitSize * -11 + unitSize * i;
        
        // Top side holes
        let wheelHole1 = makeCylinder(outerRadius, 0.8, [0, 0, 0], [0, 0.8, 0])
            .translate(xPos, unitSize * 8 - 0.4, wheelZ);
        part = part.cut(wheelHole1);
        
        let wheelHole2 = makeCylinder(outerRadius, 0.8, [0, 0, 0], [0, 0.8, 0])
            .translate(xPos, unitSize * 7 - 0.4, wheelZ);
        part = part.cut(wheelHole2);
        
        let wheelHole3 = makeCylinder(innerRadius, unitSize, [0, 0, 0], [0, unitSize, 0])
            .translate(xPos, unitSize * 7, wheelZ);
        part = part.cut(wheelHole3);
    }
    
    // Wheel holes (side 2 - bottom side)
    for (let i = 1; i <= 21; i++) {
        // Skip certain positions
        if ([3, 4, 5, 10, 11, 12, 17, 18, 19].includes(i)) {
            continue;
        }
        
        const xPos = unitSize * -11 + unitSize * i;
        
        // Bottom side holes
        let wheelHole4 = makeCylinder(outerRadius, 0.8, [0, 0, 0], [0, 0.8, 0])
            .translate(xPos, unitSize * -8 - 0.4, wheelZ);
        part = part.cut(wheelHole4);
        
        let wheelHole5 = makeCylinder(outerRadius, 0.8, [0, 0, 0], [0, 0.8, 0])
            .translate(xPos, unitSize * -7 - 0.4, wheelZ);
        part = part.cut(wheelHole5);
        
        let wheelHole6 = makeCylinder(innerRadius, unitSize, [0, 0, 0], [0, unitSize, 0])
            .translate(xPos, unitSize * -8, wheelZ);
        part = part.cut(wheelHole6);
    }
    
    // Supports (long rails)
    let support1 = makeBox(
        [-unitSize * 10, -unitSize * 0.5, 0],
        [unitSize * 10, unitSize * 0.5, unitHeight]
    ).translate(0, unitSize * 3.5, 0);
    part = part.fuse(support1);
    
    let support2 = makeBox(
        [-unitSize * 10, -unitSize * 0.5, 0],
        [unitSize * 10, unitSize * 0.5, unitHeight]
    ).translate(0, unitSize * -3.5, 0);
    part = part.fuse(support2);
    
    // Battery holders
    const batteryHolderZ1 = unitHeight * 1;
    const batteryHolderZ2 = 0;
    
    // Side battery holders
    let batteryHolder1 = makeBox(
        [-unitSize * 0.5, -unitSize * 1, 0],
        [unitSize * 0.5, unitSize * 1, unitHeight * 2]
    ).translate(unitSize * -9.5, 0, batteryHolderZ1);
    part = part.fuse(batteryHolder1);
    
    let batteryHolder2 = makeBox(
        [-unitSize * 0.5, -unitSize * 1, 0],
        [unitSize * 0.5, unitSize * 1, unitHeight * 2]
    ).translate(unitSize * 9.5, 0, batteryHolderZ1);
    part = part.fuse(batteryHolder2);
    
    // Bottom supports for battery
    let batterySupport1 = makeBox(
        [-unitSize * 0.5, -unitSize * 3, 0],
        [unitSize * 0.5, unitSize * 3, unitHeight]
    ).translate(unitSize * -9.5, 0, batteryHolderZ2);
    part = part.fuse(batterySupport1);
    
    let batterySupport2 = makeBox(
        [-unitSize * 0.5, -unitSize * 3, 0],
        [unitSize * 0.5, unitSize * 3, unitHeight]
    ).translate(unitSize * 9.5, 0, batteryHolderZ2);
    part = part.fuse(batterySupport2);
    
    // Additional battery holder supports
    const supportPositions = [
        [unitSize * 7, unitSize * 3.5],
        [unitSize * 7, unitSize * -3.5],
        [unitSize * -7, unitSize * 3.5],
        [unitSize * -7, unitSize * -3.5],
        [0, unitSize * 3.5],
        [0, unitSize * -3.5],
    ];
    
    for (const pos of supportPositions) {
        let holder = makeBox(
            [-unitSize * 1, -unitSize * 0.5, 0],
            [unitSize * 1, unitSize * 0.5, unitHeight * 2]
        ).translate(pos[0], pos[1], batteryHolderZ1);
        part = part.fuse(holder);
    }
    
    // Battery compartment cutout
    let batteryCompartment = makeBox(
        [-unitSize * 9, -unitSize * 3, 0],
        [unitSize * 9, unitSize * 3, unitHeight]
    ).translate(0, 0, 0);
    part = part.cut(batteryCompartment);
    
    // Mounting screw holes
    const screwRadius = 1.5;
    const screwHeight = unitHeight * 3;
    const screwZ = 0;
    
    const screwPositions = [
        [unitSize * 0,    unitSize * 3.5,  screwZ],
        [unitSize * 0,    unitSize * -3.5, screwZ],
        [unitSize * 7,    unitSize * 3.5,  screwZ],
        [unitSize * 7,    unitSize * -3.5, screwZ],
        [unitSize * -7,   unitSize * 3.5,  screwZ],
        [unitSize * -7,   unitSize * -3.5, screwZ],
        [unitSize * -9.5, 0,               screwZ],
        [unitSize * 9.5,  0,               screwZ],
    ];
    
    for (const pos of screwPositions) {
        let screwHole = makeCylinder(screwRadius, screwHeight, [0, 0, 0], [0, 0, screwHeight])
            .translate(pos[0], pos[1], pos[2]);
        part = part.cut(screwHole);
    }
    
    // Apply fillet to all edges that are parallel to Z-axis
    part = part.fillet(2, (e) => e.inDirection('Z'));
    
    return part;
}