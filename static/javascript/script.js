
var btn = document.querySelector('.mouse-cursor-gradient-tracking')

btn.onmousemove = function(e)
{
  var x = e.pageX - btn.offsetLeft - btn.offsetParent.offsetLeft
  var y = e.pageY - btn.offsetTop - btn.offsetParent.offsetTop
  btn.style.setProperty('--x', x + 'px')
  btn.style.setProperty('--y', y + 'px')
}

function readURL(input) {
            if (input.files && input.files[0]) {
                var reader = new FileReader();

                reader.onload = function (e) {
                    $('#blah')
                        .attr('src', e.target.result);
                };

                reader.readAsDataURL(input.files[0]);
            }
        }


function previewFile() {
    var preview = document.getElementById("blah");
    var file    = document.querySelector('input[type=file]').files[0];
    var reader  = new FileReader();
    
    reader.addEventListener("load", function () {
        preview.src = reader.result;
    }, false);
    
    if (file) {
        reader.readAsDataURL(file);
    }
    }