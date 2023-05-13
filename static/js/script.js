const pokemonBox = document.querySelector('.pokemon-box');

// Quando o formulário é enviado
document.querySelector('form').addEventListener('submit', (event) => {
  event.preventDefault(); // impede o envio do formulário padrão
  const searchQuery = document.getElementById('search').value;
  fetch(`/search?q=${searchQuery}`) // substitua por sua rota de busca
    .then(response => response.json())
    .then(data => {
      if (data.pokemon) {
        pokemonBox.classList.remove('leave');
        pokemonBox.classList.add('enter');
        setTimeout(() => {
          pokemonBox.classList.remove('enter');
          pokemonBox.classList.remove('sliding-box');
        }, 500);
      } else {
        pokemonBox.classList.remove('enter');
        pokemonBox.classList.add('leave');
        setTimeout(() => {
          pokemonBox.classList.remove('leave');
        }, 500);
      }
    });
});
