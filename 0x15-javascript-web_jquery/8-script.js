$(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, status) {
    if (status === 'success') {
      const movies = data.results;
      for (const movie in movies) {
        $('#list_movies').append('<li>' + movies[movie].title + '</li>');
      }
    }
  });
});
