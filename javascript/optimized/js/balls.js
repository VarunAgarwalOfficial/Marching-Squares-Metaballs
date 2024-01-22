class Ball {
    constructor() {
        this.radius = random(20, 30);
        this.x = random(width - this.radius);
        this.y = random(height - this.radius);
        this.dx = random(-20, 20);
        this.dy = random(-20, 20);
    }

    update() {
        this.x += this.dx;
        this.y += this.dy;
        if (this.x > width - this.radius || this.x < this.radius) {
            this.dx *= -1;
        }
        if (this.y > height - this.radius || this.y < this.radius) {
            this.dy *= -1;
        }
    }

}