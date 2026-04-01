const { makeBox, makeCylinder } = replicad;

const unitSize = 8.0;           // lego unit size
const unitHeight = 9.6;         // lego brick height
const holeInnerDiameter = 4.8;  // lego hole inner diameter
const holeOuterDiameter = 6.2;  // lego hole outer diameter

const main = () => {
    // Base
    const length = unitSize * 7;
    const width = unitSize * 12;
    const height = unitHeight / 3;
    
    let part = makeBox(
        [-length/2, -width/2, 0],
        [length/2, width/2, height]
    );
    
    // Cutout
    const cutoutLength = unitSize * 4;
    const cutoutWidth = unitSize * 10;
    const cutoutHeight = unitHeight / 3;
    
    let cutout = makeBox(
        [-cutoutLength/2, -cutoutWidth/2, 0],
        [cutoutLength/2, cutoutWidth/2, cutoutHeight]
    ).translate(unitSize * 0.5, 0, 0);
    part = part.cut(cutout);
    
    // Mounting screw holes
    const screwRadius = 1.5;
    const screwHeight = unitHeight;
    
    const screwPositions = [
        [unitSize * -2.5, unitSize * 5.5, 0],
        [unitSize * -2.5, unitSize * -5.5, 0],
        [unitSize * 3, unitSize * 4, 0],
        [unitSize * 3, unitSize * -4, 0],
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