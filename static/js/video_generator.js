let captions = document.getElementById("captions");
let VideoT = document.getElementById("VideoT");
let setting = document.getElementById("setting");
let videoTypeList = document.getElementById("videoType-list");
let inputcaption = document.getElementById("input-caption");
let savebutton = document.getElementById("save-button");
let editbutton = document.getElementById("edit-button");
let forsave = document.getElementById("for-save");
let foredit = document.getElementById("for-edit");
let MusicBackground = document.getElementById("MusicBackground");
let MusicType = document.getElementById("MusicType");
let captionBtn = document.getElementById("captiontype-btn");
let captionType = document.getElementById("captionType");

captions.addEventListener("click", () => {
  videoTypeList.classList.remove("videotype-list");
  videoTypeList.classList.add("videotype-list-disable");
  inputcaption.classList.add("inputcaption");
  inputcaption.classList.remove("inputcaptiont-disable");
  VideoT.classList.remove("active_p");
  setting.classList.remove("active_p");
  captions.classList.add("active_p");
});
VideoT.addEventListener("click", () => {
  captions.classList.remove("active_p");
  VideoT.classList.add("active_p");
  setting.classList.remove("active_p");
  inputcaption.classList.remove("inputcaption");
  inputcaption.classList.add("inputcaptiont-disable");
  videoTypeList.classList.add("videotype-list");
  videoTypeList.classList.remove("videotype-list-disable");
});
setting.addEventListener("click", () => {
  videoTypeList.classList.remove("videotype-list");
  videoTypeList.classList.add("videotype-list-disable");
  inputcaption.classList.remove("inputcaption");
  inputcaption.classList.add("inputcaptiont-disable");
  captions.classList.remove("active_p");
  VideoT.classList.remove("active_p");
  setting.classList.add("active_p");
});
savebutton.addEventListener("click", () => {
  forsave.classList.add("active-caption");
  foredit.classList.remove("active-caption");
});
editbutton.addEventListener("click", () => {
  forsave.classList.remove("active-caption");
  foredit.classList.add("active-caption");
});
MusicBackground.addEventListener("click", () => {
  MusicBackground.style.background = "rgb(255 90 31 / 1)";
  MusicBackground.style.color = "#fff";
  MusicType.style.cursor = "pointer";
  MusicType.disabled = false;
});
captionBtn.addEventListener("click", () => {
  captionBtn.style.background = "rgb(255 90 31 / 1)";
  captionBtn.style.color = "#fff";
  captionType.style.cursor = "pointer";
  captionType.disabled = false;
});
