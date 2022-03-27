$(document).ready(function() {
  // $('.map').maphilight();
  $('.sub-map').rwdImageMaps();
});

$('area').on('click', function() {
  let target = $(this).attr('alt');
  $.ajax({
      type: "GET",
      url: "/distance/" + target,
      data: target,
      success: function(data) {
          let isParking = document.getElementById("is-parking")
          let title = document.getElementById("title");
          let nearest = document.getElementById("nearest");
          let distance = document.getElementById("distance");
          let walkingTime = document.getElementById("walking-time");
          
          if (data["is_parking"]) {
            isParking.innerHTML = "附近的建築物： "
          }
          else {
            isParking.innerHTML = "最近的停車場： "
          }
          title.innerHTML = target;
          nearest.innerHTML = data["result"][0]["target"];
          distance.innerHTML = "距離： " + data["result"][0]["info"]["distance"];
          walkingTime.innerHTML = "步行時間： " + data["result"][0]["info"]["walking_time"];
      }
  });
});