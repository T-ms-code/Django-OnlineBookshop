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
-- Data for Name: aplicatie_autor; Type: TABLE DATA; Schema: proiect; Owner: mihai
--

INSERT INTO proiect.aplicatie_autor (id, nume, prenume, data_nastere, data_deces, nationalitate, descriere, premii) VALUES (1, 'Preda', 'Marin', '1922-08-05', '1980-05-16', 'Romana', '├Än anul 1941, Marin Preda ╚Öi-a g─âsit un post de corector la ziarul ΓÇ£TimpulΓÇ¥, unde a debutat un an mai t├órziu cu schi╚¢a ΓÇ£P├órlitulΓÇ£. ├Äntre anii 1943-1945, c├ót a ├«ndurat stagiul militar, ╚Öi-a ├«ntrerupt activitatea editorial─â.

Marin Preda frecventeaz─â des ╚Öi cenaclul ΓÇ£Zbur─âtorulΓÇ¥ condus de criticul Eugen Lovinescu, acolo unde nuvela sa ΓÇ£CalulΓÇ¥ face o bun─â impresie celor prezen╚¢i. De╚Öi riscant, ulterior ╚Öi-a f─âcut curaj ╚Öi a prezentat mai multe momente de-acolo ├«n romane precum ΓÇ£Via╚¢─â ca o prad─âΓÇ£ ╚Öi ΓÇ£DelirulΓÇ£. Dup─â ce a revenit la Bucure╚Öti, deloc u╚Öor, s-a reintegrat ├«n lumea presei ╚Öi a devenit corector la publica╚¢ia ΓÇ£Rom├ónia liber─âΓÇ£. Marin Preda trece prin redac╚¢iile mai multor ziare ╚Öi abia ├«n 1955 public─â ΓÇ£Morome╚¢iiΓÇ¥. Un lucru mai pu╚¢in ╚Ötiut este faptul c─â romanul a fost publicat la insisten╚¢ele iubitei sale, care a g─âsit manuscrisul din ├«nt├ómplare ├«ntr-un sertar. ├Än anul imediat urm─âtor, Marin Preda prime╚Öte Premiul de Stat, chiar pentru romanul ΓÇ£Morome╚¢iiΓÇ¥.', 'Premiul de Stat pentru Literatur─â, Premiul Uniunii, Ordinul Muncii, etc.');
INSERT INTO proiect.aplicatie_autor (id, nume, prenume, data_nastere, data_deces, nationalitate, descriere, premii) VALUES (2, 'Eliade', 'Mircea', '1907-03-02', '1988-04-22', 'Romana', 'Mircea Eliade (1907ΓÇô1986) a fost un filozof, istoric al religiilor ╚Öi scriitor rom├ón de renume interna╚¢ional. Este cunoscut pentru cercet─ârile sale ├«n domeniul mitologiei, religiilor ╚Öi istoriei spiritualit─â╚¢ii umane, abord├ónd religia dintr-o perspectiv─â comparativ─â ╚Öi antropologic─â. Eliade a fost autorul unor lucr─âri fundamentale, precum ΓÇ₧Tratat de istorie a religiilorΓÇ¥ ╚Öi ΓÇ₧Mitul eternei re├«ntoarceriΓÇ¥. De asemenea, a fost un proeminent eseist ╚Öi romancier, cu lucr─âri literare importante, cum ar fi ΓÇ₧MaitreyiΓÇ¥ ╚Öi ΓÇ₧Noaptea de S├ónzieneΓÇ¥. Opera sa a influen╚¢at profund studiile religioase ╚Öi filozofia contemporan─â.', 'Premiul Herder (1970), Premiul Universit─â╚¢ii din Chicago (1969)');
INSERT INTO proiect.aplicatie_autor (id, nume, prenume, data_nastere, data_deces, nationalitate, descriere, premii) VALUES (3, 'Rebreanu', 'Liviu', '1885-11-27', '1885-08-01', 'Romana', 'Liviu Rebreanu (1885ΓÇô1944) a fost un important scriitor ╚Öi dramaturg rom├ón, cunoscut pentru realismul s─âu profund ╚Öi pentru portretizarea societ─â╚¢ii rom├óne╚Öti. Cele mai celebre lucr─âri ale sale includ romanul ΓÇ₧IonΓÇ¥, o analiz─â a conflictelor sociale ╚Öi psihologice din mediul rural, ╚Öi ΓÇ₧R─âscoalaΓÇ¥, care abordeaz─â luptele ╚¢─âranilor pentru drepturi ╚Öi libertate. Rebreanu a fost ╚Öi un autor de teatru, iar piesele sale, precum ΓÇ₧P─âdurea sp├ónzura╚¢ilorΓÇ¥, au explorat teme legate de destinul uman ╚Öi natura conflictelor. A fost un scriitor angajat, care a reflectat asupra realit─â╚¢ilor politice ╚Öi sociale ale vremii sale. Rebreanu este considerat unul dintre cei mai mari autori ai literaturii rom├óne din secolul XX.', 'Premiul Na╚¢ional pentru Literatur─â (1929), Premiul Academiei Rom├óne (1933) etc');
INSERT INTO proiect.aplicatie_autor (id, nume, prenume, data_nastere, data_deces, nationalitate, descriere, premii) VALUES (4, 'Dostoievski', 'Feodor', '1888-05-07', '1821-01-08', 'Rusa', 'Feodor Dostoievski (1821ΓÇô1881) a fost un scriitor rus de renume mondial, cunoscut pentru explorarea ad├ónc─â a psihologiei umane ╚Öi a conflictelor morale. Printre cele mai importante lucr─âri ale sale se num─âr─â ΓÇ₧Crim─â ╚Öi pedeaps─âΓÇ¥, ΓÇ₧Fra╚¢ii KaramazovΓÇ¥ ╚Öi ΓÇ₧IdiotulΓÇ¥, ├«n care abordeaz─â teme precum libertatea, vinov─â╚¢ia, m├óntuirea ╚Öi natura uman─â. Dostoievski a tr─âit o via╚¢─â marcat─â de suferin╚¢e personale, inclusiv o condamnare la munc─â silnic─â ╚Öi o perioad─â de exil ├«n Siberia. Filosofia sa a influen╚¢at profund literatura ╚Öi g├óndirea filozofic─â, av├ónd o mare influen╚¢─â asupra existen╚¢ialismului ╚Öi psihologiei moderne. Este considerat unul dintre cei mai mari scriitori ai literaturii universale.', 'Nu a primit premii importante ├«n timpul vie╚¢ii sale.');
INSERT INTO proiect.aplicatie_autor (id, nume, prenume, data_nastere, data_deces, nationalitate, descriere, premii) VALUES (5, 'Zafon', 'Carlos Ruiz', '1964-09-24', '2020-06-19', 'Spaniola', 'A fost un scriitor ╚Öi scenarist spaniol, cunoscut la nivel interna╚¢ional pentru romanele sale pline de mister ╚Öi atmosfer─â. Cel mai faimos dintre ele este ΓÇ₧Umbra v├óntuluiΓÇ¥, primul volum din seria ΓÇ₧Cimitirul c─âr╚¢ilor uitateΓÇ¥, o poveste captivant─â despre iubire, prietenie ╚Öi r─âzbunare, care exploreaz─â leg─âtura dintre literatur─â ╚Öi via╚¢a cotidian─â. Zaf├│n a fost, de asemenea, un autor de literatur─â pentru tineri ╚Öi un important scenarist de televiziune ╚Öi film. Opera sa a fost tradus─â ├«n multe limbi ╚Öi a c├ó╚Ötigat numeroase premii. A influen╚¢at profund literatura contemporan─â, ├«mbin├ónd elemente de realism magic cu tehnici narative sofisticate.', 'Premiul de Literatur─â "Planeta" (1993) etc.');
INSERT INTO proiect.aplicatie_autor (id, nume, prenume, data_nastere, data_deces, nationalitate, descriere, premii) VALUES (6, 'Asimov', 'Isaac', '1920-01-02', '1992-04-06', 'Rusa', 'Isaac Asimov a fost un prolific scriitor ╚Öi biochimist american de origine rus─â, cunoscut mai ales pentru operele sale de science-fiction ╚Öi lucr─ârile de popularizare a ╚Ötiin╚¢ei.', 'Premiul Hugo, Premiul Bram Stoker etc.');
INSERT INTO proiect.aplicatie_autor (id, nume, prenume, data_nastere, data_deces, nationalitate, descriere, premii) VALUES (7, 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'Ion', '1980-08-05', NULL, 'Rom├ón─â', 'Autorul are v├órsta de 28 ani.', 'Premiul scriitorilor');
INSERT INTO proiect.aplicatie_autor (id, nume, prenume, data_nastere, data_deces, nationalitate, descriere, premii) VALUES (8, 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'Ion', '1980-08-05', NULL, 'Rom├ón─â', 'Autorul are v├órsta de 28 ani.', 'Premiul scriitorilor');
INSERT INTO proiect.aplicatie_autor (id, nume, prenume, data_nastere, data_deces, nationalitate, descriere, premii) VALUES (9, 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'Ion', '1980-08-05', NULL, 'Rom├ón─â', 'Autorul are v├órsta de 28 ani.', 'Premiul scriitorilor');
INSERT INTO proiect.aplicatie_autor (id, nume, prenume, data_nastere, data_deces, nationalitate, descriere, premii) VALUES (10, 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'Ion', '1980-08-05', NULL, 'Rom├ón─â', 'Autorul are v├órsta de 28 ani.', 'Premiul scriitorilor');
INSERT INTO proiect.aplicatie_autor (id, nume, prenume, data_nastere, data_deces, nationalitate, descriere, premii) VALUES (11, 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'Ion', '1980-08-05', NULL, 'Rom├ón─â', 'Autorul are v├órsta de 28 ani.', 'Premiul scriitorilor');
INSERT INTO proiect.aplicatie_autor (id, nume, prenume, data_nastere, data_deces, nationalitate, descriere, premii) VALUES (12, 'Coldea', 'Camil', '1977-09-15', '2010-09-15', 'Rom├ón─â', 'Autorul a murit la v├órsta de 33 ani.', 'Premiul scriitorilor');
INSERT INTO proiect.aplicatie_autor (id, nume, prenume, data_nastere, data_deces, nationalitate, descriere, premii) VALUES (13, 'Coldea', 'Marius', '1977-09-15', '2010-09-15', 'Rom├ón─â', 'Autorul a murit la v├órsta de 33 ani.', 'Premiul scriitorilor');
INSERT INTO proiect.aplicatie_autor (id, nume, prenume, data_nastere, data_deces, nationalitate, descriere, premii) VALUES (14, 'Dragomir', 'Mitica', '1977-09-15', '2007-09-15', 'Rom├ón─â', 'Autorul a murit la v├órsta de 30 ani.', 'Premiul scriitorilor');
INSERT INTO proiect.aplicatie_autor (id, nume, prenume, data_nastere, data_deces, nationalitate, descriere, premii) VALUES (15, 'Dragomir', 'Mitica', '1960-08-05', '1985-08-05', 'Romana', 'Autorul a murit la varsta de 25 ani.', 'Premiul scriitorilor');
INSERT INTO proiect.aplicatie_autor (id, nume, prenume, data_nastere, data_deces, nationalitate, descriere, premii) VALUES (16, 'Dragomir', 'Mitica', '1960-08-05', '1985-08-05', 'Romana', 'Autorul a murit la varsta de 25 ani.', 'Premiul scriitorilor');
INSERT INTO proiect.aplicatie_autor (id, nume, prenume, data_nastere, data_deces, nationalitate, descriere, premii) VALUES (17, 'Dragomir', 'Mitica', '1960-08-05', '1985-08-05', 'Romana', 'Autorul a murit la varsta de 25 ani.', 'Premiul scriitorilor');
INSERT INTO proiect.aplicatie_autor (id, nume, prenume, data_nastere, data_deces, nationalitate, descriere, premii) VALUES (18, 'Cartarescu', 'Mircea', '1981-01-01', NULL, 'Romana', 'Autorul are varsta de 42 ani.', 'Premiul Uniunii Scriitorilor din Rom├ónia');
INSERT INTO proiect.aplicatie_autor (id, nume, prenume, data_nastere, data_deces, nationalitate, descriere, premii) VALUES (19, 'Cartarescu', 'Mircea', '1981-01-01', NULL, 'Romana', 'Autorul are varsta de 50 ani.', 'Premiul Uniunii Scriitorilor din Rom├ónia');
INSERT INTO proiect.aplicatie_autor (id, nume, prenume, data_nastere, data_deces, nationalitate, descriere, premii) VALUES (20, 'Cartarescu', 'Mircea', '1981-01-01', NULL, 'Romana', 'Autorul are varsta de 50 ani.', 'Premiul Uniunii Scriitorilor din Rom├ónia');
INSERT INTO proiect.aplicatie_autor (id, nume, prenume, data_nastere, data_deces, nationalitate, descriere, premii) VALUES (21, 'Cartarescu', 'Mircea', '1981-01-01', NULL, 'Romana', 'Autorul are varsta de 50 ani.', 'Premiul Uniunii Scriitorilor din Rom├ónia');
INSERT INTO proiect.aplicatie_autor (id, nume, prenume, data_nastere, data_deces, nationalitate, descriere, premii) VALUES (22, 'Cartarescu', 'Mircea', '1981-01-01', NULL, 'Romana', 'Autorul are varsta de 50 ani.', 'Premiul Uniunii Scriitorilor din Rom├ónia');
INSERT INTO proiect.aplicatie_autor (id, nume, prenume, data_nastere, data_deces, nationalitate, descriere, premii) VALUES (23, 'Cartarescu', 'Mircea', '1981-01-01', NULL, 'Romana', 'Autorul are varsta de 50 ani.', 'Premiul Uniunii Scriitorilor din Rom├ónia');
INSERT INTO proiect.aplicatie_autor (id, nume, prenume, data_nastere, data_deces, nationalitate, descriere, premii) VALUES (24, 'Cartarescu', 'Mircea', '1981-01-01', NULL, 'Romana', 'Autorul are varsta de 50 ani.', 'Premiul Uniunii Scriitorilor din Rom├ónia');
INSERT INTO proiect.aplicatie_autor (id, nume, prenume, data_nastere, data_deces, nationalitate, descriere, premii) VALUES (25, 'Cartarescu', 'Mircea', '1981-01-01', NULL, 'Romana', 'Autorul are varsta de 43 ani.', 'Premiul Uniunii Scriitorilor din Rom├ónia');


--
-- Name: aplicatie_autor_id_seq; Type: SEQUENCE SET; Schema: proiect; Owner: mihai
--

SELECT pg_catalog.setval('proiect.aplicatie_autor_id_seq', 25, true);


--
-- PostgreSQL database dump complete
--

