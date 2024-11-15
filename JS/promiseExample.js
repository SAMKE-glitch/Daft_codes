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

(async function handlePromise () {
	try {
		let result = await myPromise;
		console.log("Promis resolved with:", result);
	} catch (error) {
		console.error("Promise rejected with:", error);
	}
}
handlePromise();
