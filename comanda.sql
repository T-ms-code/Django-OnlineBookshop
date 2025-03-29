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
-- Data for Name: aplicatie_comanda; Type: TABLE DATA; Schema: proiect; Owner: mihai
--

INSERT INTO proiect.aplicatie_comanda (id, nr_produse, pret_total, data_concepere, data_livrare, firma_livratoare, adresa_livrare, mod_plata) VALUES (1, 1, 70.00, '2024-11-21', '2024-11-21', 'Fan Courier', 'Arge╚Ö, Topoloveni,  Bl. B3, Scara A, Ap. 6', 'card');
INSERT INTO proiect.aplicatie_comanda (id, nr_produse, pret_total, data_concepere, data_livrare, firma_livratoare, adresa_livrare, mod_plata) VALUES (2, 3, 240.00, '2024-11-21', '2024-10-03', 'Cargus', 'Ploiesti, Plopeni,  Nr. 167', 'card');


--
-- Name: aplicatie_comanda_id_seq; Type: SEQUENCE SET; Schema: proiect; Owner: mihai
--

SELECT pg_catalog.setval('proiect.aplicatie_comanda_id_seq', 2, true);


--
-- PostgreSQL database dump complete
--

