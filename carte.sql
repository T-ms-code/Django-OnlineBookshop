--
-- PostgreSQL database dump
--

-- Dumped from database version 17.0
-- Dumped by pg_dump version 17.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatie_carte; Type: TABLE DATA; Schema: proiect; Owner: mihai
--

INSERT INTO proiect.aplicatie_carte (id, titlu, nr_pagini, data_publicatie, coperta, pret, stoc, autor_id) VALUES (2, 'La ╚¢ig─ânci', 180, '1959-01-01', '', 20.00, 'neepuizat', 2);
INSERT INTO proiect.aplicatie_carte (id, titlu, nr_pagini, data_publicatie, coperta, pret, stoc, autor_id) VALUES (3, 'Noaptea de S├ónziene', 400, '1939-01-01', '', 37.00, 'epuizat', 2);
INSERT INTO proiect.aplicatie_carte (id, titlu, nr_pagini, data_publicatie, coperta, pret, stoc, autor_id) VALUES (5, 'Idiotul', 680, '1869-01-01', '', 33.00, 'neepuizat', 4);
INSERT INTO proiect.aplicatie_carte (id, titlu, nr_pagini, data_publicatie, coperta, pret, stoc, autor_id) VALUES (7, 'Funda╚¢ia', 256, '1951-01-01', '', 42.00, 'neepuizat', 6);
INSERT INTO proiect.aplicatie_carte (id, titlu, nr_pagini, data_publicatie, coperta, pret, stoc, autor_id) VALUES (1, 'Morome╚¢ii', 850, '1967-01-01', 'coperta1.jpeg', 80.00, 'neepuizat', 1);
INSERT INTO proiect.aplicatie_carte (id, titlu, nr_pagini, data_publicatie, coperta, pret, stoc, autor_id) VALUES (4, 'Ion', 900, '1920-01-01', '', 55.00, 'neepuizat', 3);
INSERT INTO proiect.aplicatie_carte (id, titlu, nr_pagini, data_publicatie, coperta, pret, stoc, autor_id) VALUES (6, 'Demonii', 986, '1872-01-01', '', 61.00, 'neepuizat', 4);


--
-- Name: aplicatie_carte_id_seq; Type: SEQUENCE SET; Schema: proiect; Owner: mihai
--

SELECT pg_catalog.setval('proiect.aplicatie_carte_id_seq', 7, true);


--
-- PostgreSQL database dump complete
--

