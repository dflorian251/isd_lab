import * as THREE from 'three';

console.log("Hello world")
var WIDTH = window.innerWidth,
	HEIGHT = window.innerHeight,
	VIEW_ANGLE = 45,
	ASPECT = WIDTH / HEIGHT,
	NEAR = .1,
	FAR = 1e4,
	container = document.querySelector(".canvas"),
	renderer = new THREE.WebGLRenderer({
		antialias: !1
	}),
	camera = new THREE.PerspectiveCamera(VIEW_ANGLE, ASPECT, NEAR, FAR),
	scene = new THREE.Scene;
scene.background = new THREE.Color("#ffffff"), scene.add(camera), renderer.setSize(WIDTH, HEIGHT), container?.appendChild(renderer.domElement);
var RADIUS = 115,
	SEGMENTS = 12,
	RINGS = 12,
	sphereMaterial = new THREE.MeshLambertMaterial({
		color: 10101610,
		wireframe: !0
	}),
	sphere = new THREE.Mesh(new THREE.SphereGeometry(RADIUS, SEGMENTS, RINGS), sphereMaterial);
sphere.position.z = -300, window.innerWidth < 768 ? sphere.position.x = window.innerWidth / 6 : sphere.position.x = window.innerWidth / 8, sphere.position.y = 0, scene.add(sphere), scene.add(new THREE.AmbientLight(16777215));
var pointLight = new THREE.PointLight(16777215, .25);
pointLight.position.z = -250, pointLight.position.x = -1e3, pointLight.position.y = 0, scene.add(pointLight);
var pointLight2 = new THREE.PointLight(16777215, .325);
pointLight2.position.z = 0, pointLight2.position.x = -700, pointLight2.position.y = 0, scene.add(pointLight2);
var pointLight3 = new THREE.PointLight(16777215, .325);

function update() {
	sphere.rotation.z += .002, sphere.rotation.y += .002, renderer.render(scene, camera), requestAnimationFrame(update)
}

function resizer() {
	window.innerWidth < 768 ? sphere.position.x = window.innerWidth / 6 : sphere.position.x = window.innerWidth / 8, renderer.setSize(window.innerWidth, window.innerHeight, !0), camera.aspect = window.innerWidth / window.innerHeight, camera.updateProjectionMatrix()
}
pointLight3.position.z = 250, pointLight3.position.x = -700, pointLight3.position.y = 0, scene.add(pointLight3), requestAnimationFrame(update), window.addEventListener("resize", resizer);
var cont = document.getElementById("waveBG"),
	vertexHeight = 15e3,
	plDefinition = 100,
	plSize = 1245e3,
	totalObjects = 1,
	bg = "#ffffff",
	meshColor = "#dedede",
	cam = new THREE.PerspectiveCamera(55, window.innerWidth / window.innerHeight, 1, 4e5);

cam.position.z = 1e4, cam.position.y = 1e4;
var sce = new THREE.Scene;
sce.fog = new THREE.Fog(bg, 1, 3e5);
var plGeo = new THREE.PlaneGeometry(plSize, plSize, plDefinition, plDefinition),
	pl = new THREE.Mesh(plGeo, new THREE.MeshBasicMaterial({
		color: meshColor,
		wireframe: !0
	}));
pl.rotation.x -= .5 * Math.PI, sce.add(pl);
var rend = new THREE.WebGLRenderer({
	alpha: !1
});

function updatePlane() {
	for (var e = 0; e < plGeo.vertices.length; e++) plGeo.vertices[e].z += Math.random() * vertexHeight - vertexHeight, plGeo.vertices[e]._myZ = plGeo.vertices[e].z
}
rend.setSize(window.innerWidth, window.innerHeight), rend.setClearColor(bg, 1), cont?.appendChild(rend.domElement), updatePlane(), render();
var count = 0;

function render() {
	requestAnimationFrame(render);
	var e = cam.position.x,
		i = cam.position.z;
	cam.position.x = e * Math.cos(.001) + i * Math.sin(.001) - 10, cam.position.z = i * Math.cos(.001) - e * Math.sin(.001) - 10, cam.lookAt(new THREE.Vector3(0, 8e3, 0));
	for (var n = 0; n < plGeo.vertices.length; n++) {
		i = +plGeo.vertices[n].z;
		plGeo.vertices[n].z = Math.sin(n + 2e-5 * count) * (plGeo.vertices[n]._myZ - .6 * plGeo.vertices[n]._myZ), pl.geometry.verticesNeedUpdate = !0, count += .1
	}
	rend.render(sce, cam)
}

function onWindowResize() {
	cam.aspect = window.innerWidth / window.innerHeight, cam.updateProjectionMatrix(), rend.setSize(window.innerWidth, window.innerHeight)
}
window.addEventListener("resize", onWindowResize, !1);
