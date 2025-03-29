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
-- Data for Name: aplicatie_recenzie; Type: TABLE DATA; Schema: proiect; Owner: mihai
--

INSERT INTO proiect.aplicatie_recenzie (id, nume_creator, prenume_creator, data_creare, continut, actualizata, verificata, carte_id) VALUES (1, 'Isac', 'Daniel', '2024-11-14', 'Minunataaa!!', false, true, 1);
INSERT INTO proiect.aplicatie_recenzie (id, nume_creator, prenume_creator, data_creare, continut, actualizata, verificata, carte_id) VALUES (2, 'Florea', 'Ionut', '2024-11-14', 'Stravroghin e raul necesar...', true, false, 6);


--
-- Name: aplicatie_recenzie_id_seq; Type: SEQUENCE SET; Schema: proiect; Owner: mihai
--

SELECT pg_catalog.setval('proiect.aplicatie_recenzie_id_seq', 2, true);


--
-- PostgreSQL database dump complete
--

