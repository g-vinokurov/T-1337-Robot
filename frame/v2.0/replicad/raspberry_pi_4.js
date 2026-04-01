const { makeBox, makeCylinder } = replicad;

const unitSize = 8.0;           // lego unit size
const unitHeight = 9.6;         // lego brick height
const holeInnerDiameter = 4.8;  // lego hole inner diameter
const holeOuterDiameter = 6.2;  // lego hole outer diameter

const main = () => {
    // Base
    const length = unitSize * 12;
    const width = unitSize * 9;
    const height = unitHeight;
    
    let part = makeBox(
        [-length/2, -width/2, 0],
        [length/2, width/2, height]
    );
    
    // Cutout
    const cutoutLength = unitSize * 9;
    const cutoutWidth = unitSize * 5;
    const cutoutHeight = unitHeight;
    
    let cutout = makeBox(
        [-cutoutLength/2, -cutoutWidth/2, 0],
        [cutoutLength/2, cutoutWidth/2, cutoutHeight]
    ).translate(0, 0, 0);
    part = part.cut(cutout);
    
    // Walls
    const wallHeight = unitHeight * 2;
    const wallZ = unitHeight;
    const wallThickness = unitSize - 2.0;
    
    // Wall at (0, unitSize * 4 + 1.0)
    let wall1 = makeBox(
        [-unitSize * 6, -wallThickness/2, 0],
        [unitSize * 6, wallThickness/2, wallHeight]
    ).translate(0, unitSize * 4 + 1.0, wallZ);
    part = part.fuse(wall1);
    
    // Wall at (unitSize * 4.5, unitSize * -4 - 1.0)
    let wall2 = makeBox(
        [-unitSize * 1.5, -wallThickness/2, 0],
        [unitSize * 1.5, wallThickness/2, wallHeight]
    ).translate(unitSize * 4.5, unitSize * -4 - 1.0, wallZ);
    part = part.fuse(wall2);
    
    // Wall at (unitSize * -5.5 - 1.0, 0)
    let wall3 = makeBox(
        [-wallThickness/2, -unitSize * 4.5, 0],
        [wallThickness/2, unitSize * 4.5, wallHeight]
    ).translate(unitSize * -5.5 - 1.0, 0, wallZ);
    part = part.fuse(wall3);
    
    // Cutout in wall at (-5.5, 0)
    let wallCutout1 = makeBox(
        [-unitSize * 0.5, -unitSize * 1, 0],
        [unitSize * 0.5, unitSize * 1, wallHeight]
    ).translate(unitSize * -5.5, 0, wallZ);
    part = part.cut(wallCutout1);
    
    // Cutout in wall at (0, unitSize * 4)
    let wallCutout2 = makeBox(
        [-unitSize * 3, -unitSize * 0.5, 0],
        [unitSize * 3, unitSize * 0.5, wallHeight]
    ).translate(0, unitSize * 4, wallZ);
    part = part.cut(wallCutout2);
    
    // Pins (cylindrical protrusions)
    const pinRadius = 1.2;
    const pinHeight = unitHeight;
    const pinZ = unitHeight;
    
    const pinPositions = [
        [unitSize * -5 + 3.5, 24.5, pinZ],
        [unitSize * -5 + 3.5, -24.5, pinZ],
        [unitSize * -5 + 3.5 + 58, 24.5, pinZ],
        [unitSize * -5 + 3.5 + 58, -24.5, pinZ],
    ];
    
    for (const pos of pinPositions) {
        let pin = makeCylinder(pinRadius, pinHeight, [0, 0, 0], [0, 0, pinHeight])
            .translate(pos[0], pos[1], pos[2]);
        part = part.fuse(pin);
    }
    
    // Apply fillet to all edges that are parallel to Z-axis
    part = part.fillet(2, (e) => e.inDirection('Z'));
    
    return part;
}