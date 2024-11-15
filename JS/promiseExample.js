#!/usr/bin/env node

let promiseArgument = (resolve, reject) => {
	setTimeout(() => {
		let currTime = new Date().getTime();
		if (currTime % 2 === 0) {
			resolve("success")
		} else {
			reject("Failed!!!")
		}
	}, 2000)
};

let myPromise = new Promise(promiseArgument)
