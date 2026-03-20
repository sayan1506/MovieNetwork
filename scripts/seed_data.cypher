
MATCH (n) DETACH DELETE n;

CREATE
  (u1:User {id: "u1", name: "Alice",
            email: "alice@mail.com",
            password: "hashed_pass_1",
            joined_at: "2024-01-10"}),
  (u2:User {id: "u2", name: "Bob",
            email: "bob@mail.com",
            password: "hashed_pass_2",
            joined_at: "2024-02-15"}),
  (u3:User {id: "u3", name: "Carol",
            email: "carol@mail.com",
            password: "hashed_pass_3",
            joined_at: "2024-03-01"}),
  (u4:User {id: "u4", name: "Dave",
            email: "dave@mail.com",
            password: "hashed_pass_4",
            joined_at: "2024-03-20"}),
  (u5:User {id: "u5", name: "Eve",
            email: "eve@mail.com",
            password: "hashed_pass_5",
            joined_at: "2024-04-05"})


CREATE
  (:Genre {name: "Sci-Fi"}),
  (:Genre {name: "Thriller"}),
  (:Genre {name: "Drama"}),
  (:Genre {name: "Mystery"})


CREATE
  (m1:Movie {id: "m1", title: "Inception",
             summary: "A thief enters dreams to plant an idea.",
             poster_url: "https://example.com/inception.jpg"}),
  (m2:Movie {id: "m2", title: "Interstellar",
             summary: "Astronauts travel through a wormhole.",
             poster_url: "https://example.com/interstellar.jpg"}),
  (m3:Movie {id: "m3", title: "The Matrix",
             summary: "A hacker discovers reality is a simulation.",
             poster_url: "https://example.com/matrix.jpg"}),
  (m4:Movie {id: "m4", title: "Dune",
             summary: "A noble family controls the desert planet Arrakis.",
             poster_url: "https://example.com/dune.jpg"}),
  (m5:Movie {id: "m5", title: "Parasite",
             summary: "A poor family schemes to work for a wealthy household.",
             poster_url: "https://example.com/parasite.jpg"}),
  (m6:Movie {id: "m6", title: "Tenet",
             summary: "A secret agent manipulates the flow of time.",
             poster_url: "https://example.com/tenet.jpg"})


MATCH (m1:Movie {id: "m1"}), (m2:Movie {id: "m2"}),
      (m3:Movie {id: "m3"}), (m4:Movie {id: "m4"}),
      (m5:Movie {id: "m5"}), (m6:Movie {id: "m6"}),
      (scifi:Genre {name: "Sci-Fi"}),
      (thriller:Genre {name: "Thriller"}),
      (drama:Genre {name: "Drama"}),
      (mystery:Genre {name: "Mystery"})
CREATE
  (m1)-[:HAS_GENRE]->(scifi),
  (m1)-[:HAS_GENRE]->(thriller),
  (m2)-[:HAS_GENRE]->(scifi),
  (m2)-[:HAS_GENRE]->(drama),
  (m3)-[:HAS_GENRE]->(scifi),
  (m3)-[:HAS_GENRE]->(thriller),
  (m4)-[:HAS_GENRE]->(scifi),
  (m4)-[:HAS_GENRE]->(drama),
  (m5)-[:HAS_GENRE]->(drama),
  (m5)-[:HAS_GENRE]->(mystery),
  (m6)-[:HAS_GENRE]->(scifi),
  (m6)-[:HAS_GENRE]->(thriller)


MATCH (u1:User {id: "u1"}), (u2:User {id: "u2"}),
      (u3:User {id: "u3"}), (u4:User {id: "u4"}),
      (u5:User {id: "u5"})
CREATE
  (u1)-[:FRIEND_OF {since: "2024-02-01"}]->(u2),
  (u2)-[:FRIEND_OF {since: "2024-02-01"}]->(u1),
  (u1)-[:FRIEND_OF {since: "2024-03-10"}]->(u3),
  (u3)-[:FRIEND_OF {since: "2024-03-10"}]->(u1),
  (u2)-[:FRIEND_OF {since: "2024-04-01"}]->(u4),
  (u4)-[:FRIEND_OF {since: "2024-04-01"}]->(u2),
  (u3)-[:FRIEND_OF {since: "2024-04-15"}]->(u5),
  (u5)-[:FRIEND_OF {since: "2024-04-15"}]->(u3)




MATCH (u1:User {id: "u1"}), (u2:User {id: "u2"}),
      (u3:User {id: "u3"}), (u4:User {id: "u4"}),
      (u5:User {id: "u5"}),
      (m1:Movie {id: "m1"}), (m2:Movie {id: "m2"}),
      (m3:Movie {id: "m3"}), (m4:Movie {id: "m4"}),
      (m5:Movie {id: "m5"}), (m6:Movie {id: "m6"})
CREATE
  (u1)-[:LIKED {rating: 4.8, liked_at: "2024-03-01"}]->(m1),
  (u1)-[:LIKED {rating: 4.5, liked_at: "2024-03-15"}]->(m2),
  (u2)-[:LIKED {rating: 4.7, liked_at: "2024-03-05"}]->(m1),
  (u2)-[:LIKED {rating: 4.9, liked_at: "2024-03-18"}]->(m3),
  (u2)-[:LIKED {rating: 4.2, liked_at: "2024-04-02"}]->(m4),
  (u3)-[:LIKED {rating: 4.6, liked_at: "2024-03-20"}]->(m2),
  (u3)-[:LIKED {rating: 4.8, liked_at: "2024-04-01"}]->(m5),
  (u3)-[:LIKED {rating: 4.3, liked_at: "2024-04-10"}]->(m6),
  (u4)-[:LIKED {rating: 4.5, liked_at: "2024-04-05"}]->(m4),
  (u4)-[:LIKED {rating: 4.7, liked_at: "2024-04-12"}]->(m6),
  (u5)-[:LIKED {rating: 4.9, liked_at: "2024-04-18"}]->(m5),
  (u5)-[:LIKED {rating: 4.4, liked_at: "2024-04-20"}]->(m3)


MATCH (u1:User {id: "u1"}), (u3:User {id: "u3"}),
      (m3:Movie {id: "m3"}), (m4:Movie {id: "m4"}),
      (m6:Movie {id: "m6"})
CREATE
  (u1)-[:WATCHED {watched_at: "2024-03-10", completed: true}]->(m3),
  (u1)-[:WATCHED {watched_at: "2024-03-25", completed: false}]->(m4),
  (u3)-[:WATCHED {watched_at: "2024-04-08", completed: true}]->(m6)