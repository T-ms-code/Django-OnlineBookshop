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
-- Data for Name: aplicatie_librarie; Type: TABLE DATA; Schema: proiect; Owner: mihai
--

INSERT INTO proiect.aplicatie_librarie (id, denumire, data_infiintare, email, telefon, tara, oras, strada) VALUES (1, 'Libr─âria Humanitas', '1991-01-01', 'libraria@humanitas.ro', '0312345678', 'Rom├ónia', 'Bucure╚Öti', 'Strada Elie Radu 1');
INSERT INTO proiect.aplicatie_librarie (id, denumire, data_infiintare, email, telefon, tara, oras, strada) VALUES (2, 'Libr─âria C─ârture╚Öti', '1990-01-01', 'libraria@carturesti.ro', '0312388678', 'Rom├ónia', 'Bucure╚Öti', 'Strada Elie Radu 1');
INSERT INTO proiect.aplicatie_librarie (id, denumire, data_infiintare, email, telefon, tara, oras, strada) VALUES (3, 'Shakespeare and Company', '1951-08-01', 'editura@shcmp.ro', '0310088678', 'Fran╚¢a', 'Paris', '37 Rue de la B├╗cherie');
INSERT INTO proiect.aplicatie_librarie (id, denumire, data_infiintare, email, telefon, tara, oras, strada) VALUES (4, 'Libris', '2009-10-19', 'contact@libris.ro', '0344488678', 'Rom├ónia', 'Bra╚Öov', 'Str. Iuliu Maniu');
INSERT INTO proiect.aplicatie_librarie (id, denumire, data_infiintare, email, telefon, tara, oras, strada) VALUES (5, 'Compania de Libr─ârii Bucure╚Öti', '1950-05-01', 'contact@clb.ro', '0344488888', 'Rom├ónia', 'Bucure╚Öti', '---');


--
-- Name: aplicatie_librarie_id_seq; Type: SEQUENCE SET; Schema: proiect; Owner: mihai
--

SELECT pg_catalog.setval('proiect.aplicatie_librarie_id_seq', 5, true);


--
-- PostgreSQL database dump complete
--

