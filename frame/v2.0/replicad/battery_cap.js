const { makeBox, makeCylinder } = replicad;

const unitSize = 8.0;           // lego unit size
const unitHeight = 9.6;         // lego brick height
const holeInnerDiameter = 4.8;  // lego hole inner diameter
const holeOuterDiameter = 6.2;  // lego hole outer diameter

const main = () => {
    const length = unitSize * 20;
    const width = unitSize * 8;
    const height = 3.2;

    let part = makeBox(
        [-length/2, -width/2, 0], 
        [length/2, width/2, height]
    );
  
    let cutout1 = makeBox(
        [-unitSize * 1.5, -unitSize * 3, 0],
        [unitSize * 1.5, unitSize * 3, unitHeight]
    ).translate(unitSize * -2.5, 0, 0);
    part = part.cut(cutout1);
    
    // Second large rectangular cutout at x = 7.5 * unitSize
    let cutout2 = makeBox(
        [-unitSize * 1.5, -unitSize * 3, 0],
        [unitSize * 1.5, unitSize * 3, unitHeight]
    ).translate(unitSize * 7.5, 0, 0);
    part = part.cut(cutout2);

    // Third large rectangular cutout at x = -7.5 * unitSize
    let cutout3 = makeBox(
        [-unitSize * 1.5, -unitSize * 3, 0],
        [unitSize * 1.5, unitSize * 3, unitHeight]
    ).translate(unitSize * -7.5, 0, 0);
    part = part.cut(cutout3);
    
    // Fourth large rectangular cutout at x = 2.5 * unitSize
    let cutout4 = makeBox(
        [-unitSize * 1.5, -unitSize * 3, 0],
        [unitSize * 1.5, unitSize * 3, unitHeight]
    ).translate(unitSize * 2.5, 0, 0);
    part = part.cut(cutout4);

    // Mounting screw holes
    const holeRadius = 1.5;
    const holeHeight = 3.2;
    
    const holePositions = [
        [unitSize * 0,    unitSize * 3.5,  0],
        [unitSize * 0,    unitSize * -3.5, 0],
        [unitSize * 7,    unitSize * 3.5,  0],
        [unitSize * 7,    unitSize * -3.5, 0],
        [unitSize * -7,   unitSize * 3.5,  0],
        [unitSize * -7,   unitSize * -3.5, 0],
        [unitSize * -9.5, 0,               0],
        [unitSize * 9.5,  0,               0],
    ];
    
    for (const pos of holePositions) {
        let hole = makeCylinder(holeRadius, holeHeight, [0, 0, 0], [0, 0, holeHeight])
            .translate(pos[0], pos[1], pos[2]);
        part = part.cut(hole);
    }
    
    // Apply fillet to all edges that are parallel to Z-axis
    part = part.fillet(2, (e) => e.inDirection('Z'));
    
    return part;
}