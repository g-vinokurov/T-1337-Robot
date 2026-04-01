const { makeBox, makeCylinder } = replicad;

const unitSize = 8.0;           // lego unit size
const unitHeight = 9.6;         // lego brick height
const holeInnerDiameter = 4.8;  // lego hole inner diameter
const holeOuterDiameter = 6.2;  // lego hole outer diameter

const main = () => {
    // Base
    const length = unitSize * 4;
    const width = unitSize * 4;
    const height = unitHeight * 2;
    
    let part = makeBox(
        [-length/2, -width/2, 0],
        [length/2, width/2, height]
    );
    
    // Mounting screw holes (through holes)
    const screwRadius = 1.5;
    const screwHeight = unitHeight * 2;
    
    const screwPositions = [
        [unitSize * 1,  unitSize * 1,  0],
        [unitSize * 1,  unitSize * -1, 0],
        [unitSize * -1, unitSize * 1,  0],
        [unitSize * -1, unitSize * -1, 0],
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
        [unitSize * 1,  unitSize * 1,  counterboreZ],
        [unitSize * 1,  unitSize * -1, counterboreZ],
        [unitSize * -1, unitSize * 1,  counterboreZ],
        [unitSize * -1, unitSize * -1, counterboreZ],
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