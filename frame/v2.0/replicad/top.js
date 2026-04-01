const { makeBox, makeCylinder } = replicad;

const unitSize = 8.0;           // lego unit size
const unitHeight = 9.6;         // lego brick height
const holeInnerDiameter = 4.8;  // lego hole inner diameter
const holeOuterDiameter = 6.2;  // lego hole outer diameter

const main = () => {
    // Base
    const length = unitSize * 26;
    const width = unitSize * 10;
    const height = unitHeight * 2;
    
    let part = makeBox(
        [-length/2, -width/2, 0],
        [length/2, width/2, height]
    );
    
    // Cutouts
    // Cutout at (unitSize * -9, 0)
    let cutout1 = makeBox(
        [-unitSize * 4, -unitSize * 3, 0],
        [unitSize * 4, unitSize * 3, unitHeight * 2]
    ).translate(unitSize * -9, 0, 0);
    part = part.cut(cutout1);
    
    // Cutout at (unitSize * 9, 0)
    let cutout2 = makeBox(
        [-unitSize * 4, -unitSize * 3, 0],
        [unitSize * 4, unitSize * 3, unitHeight * 2]
    ).translate(unitSize * 9, 0, 0);
    part = part.cut(cutout2);
    
    // Cutout at (0, 0) with fixed dimensions 44x22
    let cutout3 = makeBox(
        [-22, -11, 0],
        [22, 11, unitHeight * 2]
    ).translate(0, 0, 0);
    part = part.cut(cutout3);
    
    // Cutout at (0, unitSize * -2.5)
    let cutout4 = makeBox(
        [-unitSize * 13, -unitSize * 2.5, 0],
        [unitSize * 13, unitSize * 2.5, unitHeight * 2]
    ).translate(0, unitSize * -2.5, 0);
    part = part.cut(cutout4);
    
    // Cutout at (unitSize * -7.5, 0) at mid-height
    let cutout5 = makeBox(
        [-unitSize * 3.5, -unitSize * 5, 0],
        [unitSize * 3.5, unitSize * 5, unitHeight * 2]
    ).translate(unitSize * -7.5, 0, unitHeight);
    part = part.cut(cutout5);
    
    // Cutout at (unitSize * 7.5, 0) at mid-height
    let cutout6 = makeBox(
        [-unitSize * 3.5, -unitSize * 5, 0],
        [unitSize * 3.5, unitSize * 5, unitHeight * 2]
    ).translate(unitSize * 7.5, 0, unitHeight);
    part = part.cut(cutout6);
    
    // Cutout at (0, unitSize * 4) at mid-height
    let cutout7 = makeBox(
        [-unitSize * 4, -unitSize * 1, 0],
        [unitSize * 4, unitSize * 1, unitHeight * 2]
    ).translate(0, unitSize * 4, unitHeight);
    part = part.cut(cutout7);
    
    // Mounting screw holes (through holes)
    const screwRadius = 1.5;
    const screwHeight = unitHeight * 2;
    
    const screwPositions = [
        [unitSize * -12, unitSize * 4,  0],
        [unitSize * -12, unitSize * -4, 0],
        [unitSize * 12,  unitSize * 4,  0],
        [unitSize * 12,  unitSize * -4, 0],
    ];
    
    for (const pos of screwPositions) {
        let screwHole = makeCylinder(screwRadius, screwHeight, [0, 0, 0], [0, 0, screwHeight])
            .translate(pos[0], pos[1], pos[2]);
        part = part.cut(screwHole);
    }
    
    // Counterbore holes (recessed areas for screw heads)
    const counterboreRadius = 3;
    const counterboreHeight = unitHeight;
    const counterboreZ = unitHeight;
    
    const counterborePositions = [
        [unitSize * -12, unitSize * 4,  counterboreZ],
        [unitSize * -12, unitSize * -4, counterboreZ],
        [unitSize * 12,  unitSize * 4,  counterboreZ],
        [unitSize * 12,  unitSize * -4, counterboreZ],
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