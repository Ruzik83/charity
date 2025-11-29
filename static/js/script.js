function toggleNav() {
    const navLinks = document.querySelector('.nav-links');
    const overlay = document.querySelector('.overlay');
    navLinks.classList.toggle('active');
    overlay.classList.toggle('active');
}

fetch("https://127.0.0.1:8000/api/help/")
  .then(response => response.json())
  .then(data => {
    data.forEach(item => {
      const card = `
        <div class="help-card">
          <h3>${item.full_name}</h3>
          <p><strong>Yordam turi:</strong> ${item.help_type}</p>
          <p>${item.description}</p>
          <p><strong>Telefon:</strong> ${item.phone}</p>
        </div>`;
      document.querySelector("#help-list").innerHTML += card;
    });
  });
