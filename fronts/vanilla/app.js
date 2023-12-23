class App {
  #baseUrl = "https://localhost:8000/api/";

  constructor() {
    this.init();
  }

  async init() {
    // await this.#fetchPokemons();
    const pokemons = await this.#fetchPokeapi();
    this.#buildItem(pokemons);
  }

  #buildItem(pokemons) {
    const list = document.querySelector("ul");
    const template = document.querySelector("#pokemon-item");

    pokemons.forEach((pokemon) => {
      const clone = template.content.cloneNode(true);

      const img = clone.querySelector("img");
      img.src = pokemon.image;

      const title = clone.querySelector("h2");
      title.textContent = `#${pokemon.id} - ${pokemon.name}`;
      const types = clone.querySelector(".types");

      const type1 = document.createElement("span");
      type1.textContent = pokemon.type1;
      type1.classList.add(pokemon.type1);
      types.appendChild(type1);

      if (pokemon.type2) {
        const type2 = document.createElement("span");
        type2.textContent = pokemon.type2;
        type2.classList.add(pokemon.type2);
        types.appendChild(type2);
      }

      list.appendChild(clone);
    });
  }

  async #fetchPokeapi() {
    const raw = await this.#request(
      new Request("https://beta.pokeapi.co/graphql/v1beta", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          query: `
            query {
              pokemon_v2_pokemon(where: {is_default: {_eq: true}}) {
                  species_id: pokemon_species_id
                  name
                  types: pokemon_v2_pokemontypes {
                      pokemon_v2_type {
                          name
                      }
                  }
              }
            }`,
        }),
      })
    );

    return raw.data.pokemon_v2_pokemon.map(({ name, species_id, types }) => ({
      name: this.#capitalize(name),
      id: species_id,
      type1: types[0].pokemon_v2_type.name,
      ...(types.length === 2 ? { type2: types[1].pokemon_v2_type.name } : {}),
      image: `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/${species_id}.png`,
    }));
  }

  #capitalize(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
  }

  async #fetchPokemons() {
    const pokemons = await this.#request(
      new Request(`${this.#baseUrl}pokemons`)
    );

    console.log("/pokemons", pokemons);
  }

  async #request(request) {
    request.headers.append("Accept", "application/json");
    // request.headers.append("Authorization", `Bearer ${this.#accessToken}`);

    var resp = await fetch(request);

    return await resp.json();
  }
}

new App();
