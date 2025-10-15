// static/js/camera.js

document.addEventListener("DOMContentLoaded", () => {
  const video = document.getElementById("video");
  const canvas = document.getElementById("canvas");
  const previewImage = document.getElementById("previewImage");
  const openCameraBtn = document.getElementById("openCameraBtn");
  const captureBtn = document.getElementById("captureBtn");
  const uploadBtn = document.getElementById("uploadBtn");
  const statusDiv = document.getElementById("status");

  let stream = null;
  let photoData = null;

  // Function to get CSRF token
  function getCSRFToken() {
    const name = "csrftoken";
    const cookies = document.cookie.split(";");
    for (let cookie of cookies) {
      const trimmed = cookie.trim();
      if (trimmed.startsWith(name + "=")) {
        return decodeURIComponent(trimmed.substring(name.length + 1));
      }
    }
    return "";
  }

  openCameraBtn.addEventListener("click", async () => {
    try {
      stream = await navigator.mediaDevices.getUserMedia({ video: true });
      video.srcObject = stream;
      video.style.display = "block";
      await video.play();
      captureBtn.disabled = false;
      statusDiv.innerText = "Camera ready. Click Capture.";
    } catch (error) {
      statusDiv.innerText = "❌ Could not access camera.";
      console.error(error);
    }
  });

  captureBtn.addEventListener("click", () => {
    const context = canvas.getContext("2d");
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    context.drawImage(video, 0, 0, canvas.width, canvas.height);

    photoData = canvas.toDataURL("image/png");
    previewImage.src = photoData;
    previewImage.style.display = "block";
    uploadBtn.disabled = false;
    statusDiv.innerText = "Photo captured. Ready to upload.";
  });

  uploadBtn.addEventListener("click", async () => {
    if (!photoData) return;

    statusDiv.innerText = "Uploading photo...";

    const response = await fetch("/customers/camera/upload/", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
        "X-CSRFToken": getCSRFToken(),
      },
      body: new URLSearchParams({ photo: photoData }),
    });

    const result = await response.json();
    if (result.success) {
      statusDiv.innerText = "✅ Photo uploaded successfully!";
      console.log("Image URL:", result.image_url);
    } else {
      statusDiv.innerText = "❌ Upload failed.";
      console.error(result);
    }
  });
});

