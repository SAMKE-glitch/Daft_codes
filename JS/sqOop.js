#!/usr/bin/env node
import Rectangle from sqOop

class Square extends Rectangle {
	constructor(height, width){
		if(height === width){
			super(height,width)
		} else {
			super(height, height);
		}
	}
};

let mySquare = new Square(5, 5)
