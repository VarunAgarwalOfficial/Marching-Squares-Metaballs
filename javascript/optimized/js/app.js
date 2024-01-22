let balls;
let size;
let hm;
let lowest_grid;
let height = 512;
let width = 1024;

function distance(p1, p2) {
    return Math.pow(p1[0] - p2[0], 2) + Math.pow(p1[1] - p2[1], 2);

}

function setup() {
    let cnv = createCanvas(1025, 513);
    size = createSlider(2, 16, 2, 2);
    cnv.parent('container');
    balls = []
    for (i = 0; i < 5; i++) {
        balls.push(new Ball());
    }
    stroke(255);
}



function calculate(i, j) {
    if ([i, j] in hm)
        return;
    let val = 0
    for (let ball of balls) {
        dis = distance([i, j], [ball.x, ball.y]);
        if (dis > 0)
            val += (ball.radius ** 2) / dis;
        else
            val = 1;
    }
    if (val > 0.2)
        hm[[i, j]] = 1;
    else
        hm[[i, j]] = 0;
}

function draw() {
    lowest_grid = size.value();
    hm = {}

    background(0);
    textSize(32)
    fill(255);
    text("Current Grid : " + lowest_grid, width - 300, height - 32);
    marchingSquares(0, width, 0, height, 16);
    for (let ball of balls) {
        ball.update();
    }
}




function marchingSquares(start_width, end_width, start_height, end_height, grid) {

    for (let i = start_width; i <= end_width; i += grid) {
        for (let j = start_height; j <= end_height; j += grid) {
            calculate(i, j);
            calculate(i + grid, j);
            calculate(i, j + grid);
            calculate(i + grid, j + grid);

            val = [hm[[i, j]], hm[[i + grid, j]], hm[[i + grid, j + grid]], hm[[i, j + grid]]].join('');

            if (val != '0000' && val != '1111' && grid > lowest_grid)
                marchingSquares(i, i + grid, j, j + grid, grid / 2);
            else if (val != '0000' && val != '1111') {

                if (val == '0001')
                    line(i, j + grid / 2, i + grid / 2, j + grid);
                else if (val == '0010')
                    line(i + grid / 2, j + grid, i + grid, j + grid / 2);
                else if (val == '0011')
                    line(i, j + grid / 2, i + grid, j + grid / 2);
                else if (val == '0100')
                    line(i + grid / 2, j, i + grid, j + grid / 2);
                else if (val == '0101') {
                    line(i, j + grid / 2, i + grid / 2, j);
                    line(i + grid / 2, j + grid, i + grid, j + grid / 2);
                } else if (val == '0110')
                    line(i + grid / 2, j, i + grid / 2, j + grid);
                else if (val == '0111')
                    line(i, j + grid / 2, i + grid / 2, j);
                else if (val == '1000')
                    line(i, j + grid / 2, i + grid / 2, j);
                else if (val == '1001')
                    line(i + grid / 2, j, i + grid / 2, j + grid);
                else if (val == '1010') {
                    line(i + grid / 2, j, i + grid, j + grid / 2);
                    line(i, j + grid / 2, i + grid / 2, j + grid);
                } else if (val == '1011')
                    line(i + grid / 2, j, i + grid, j + grid / 2);
                else if (val == '1100')
                    line(i, j + grid / 2, i + grid, j + grid / 2);
                else if (val == '1101')
                    line(i + grid / 2, j + grid, i + grid, j + grid / 2);
                else if (val == '1110')
                    line(i, j + grid / 2, i + grid / 2, j + grid);
            }
        }

    }
}