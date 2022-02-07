function getImageWidth(img)
{ alert("image width : " + img.width);
}


function setDivWidth()
{ var imgWidth = document.getElementById("accueil").width;
  document.getElementById("divFormationDjango").style.width = imgWidth+"px";
}

function setSectionPosition()
{ var bodyHeight = document.body.clientHeight;
  alert("body height : " + bodyHeight + " - " + bodyHeight/4);
  document.getElementById("passSection").style.marginTop = (bodyHeight/4)+"px";
}
