document.addEventListener('DOMContentLoaded', () => {
    let h_e = document.getElementById('hello');

    async function fetchAndDisplayTranslation() {
      try {
        const response = await fetch(
          'https://hellosalut.stefanbohacek.dev/?lang=fr'
        );
        if (!response.ok)
          throw new Error(`HTTP error! Status: ${response.status}`);
        const translation = await response.text();
        h_e.textContent = translation;
      } catch (error) {
        console.error('Fetch error:', error);
      }
    }
  
    fetchAndDisplayTranslation();
  });
