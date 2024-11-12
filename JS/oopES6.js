#!/usr/bin/env node

class Rectangle {
	constructor(height, width) {
		this.height = height;
		this.width = width;

		console.log("Rectangle Created")
		console.log("Height "+this.height);
		console.log("Width "+this.width);
	}
};

export default Rectangle
let myRectangle = new Rectangle(10, 5)
