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
-- Data for Name: aplicatie_editura; Type: TABLE DATA; Schema: proiect; Owner: mihai
--

INSERT INTO proiect.aplicatie_editura (id, denumire, data_infiintare, email, tara, oras, strada) VALUES (1, 'Editura Humanitas', '1990-01-01', 'editura@humanitas.ro', 'Rom├ónia', 'Bucure╚Öti', '---');
INSERT INTO proiect.aplicatie_editura (id, denumire, data_infiintare, email, tara, oras, strada) VALUES (2, 'Editura Polirom', '1990-01-01', 'polirom@polirom.ro', 'Rom├ónia', 'Bucure╚Öti', '---');
INSERT INTO proiect.aplicatie_editura (id, denumire, data_infiintare, email, tara, oras, strada) VALUES (3, 'Gallimard', '1990-01-01', 'contact@gallimard.fr', 'Fran╚¢a', 'Paris', '5 Rue de la Maison-Blanche');
INSERT INTO proiect.aplicatie_editura (id, denumire, data_infiintare, email, tara, oras, strada) VALUES (4, 'Oneworld Publications', '1986-04-08', 'contact@oneworld-publications.com', 'Marea Britanie', 'Londra', '10 Bloomsbury Street, Londra WC1B 3SR, UK');
INSERT INTO proiect.aplicatie_editura (id, denumire, data_infiintare, email, tara, oras, strada) VALUES (5, 'Grupul Editorial Litera', '1989-01-01', 'contact@litera.ro', 'Rom├ónia', 'Bucure╚Öti', 'Str. Sf. Laz─âr');


--
-- Name: aplicatie_editura_id_seq; Type: SEQUENCE SET; Schema: proiect; Owner: mihai
--

SELECT pg_catalog.setval('proiect.aplicatie_editura_id_seq', 5, true);


--
-- PostgreSQL database dump complete
--

