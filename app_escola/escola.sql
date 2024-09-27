PGDMP     3                    |            escola    15.8    15.3                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16505    escola    DATABASE     h   CREATE DATABASE escola WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'C';
    DROP DATABASE escola;
                postgres    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
                pg_database_owner    false                       0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                   pg_database_owner    false    5            �            1259    16507    alunos    TABLE     �   CREATE TABLE public.alunos (
    id integer NOT NULL,
    nome character varying(100) NOT NULL,
    cpf character(11) NOT NULL,
    turma character varying(10) NOT NULL
);
    DROP TABLE public.alunos;
       public         heap    postgres    false    5            �            1259    16506    alunos_id_seq    SEQUENCE     �   CREATE SEQUENCE public.alunos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.alunos_id_seq;
       public          postgres    false    218    5                       0    0    alunos_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.alunos_id_seq OWNED BY public.alunos.id;
          public          postgres    false    217            x           2604    16510 	   alunos id    DEFAULT     f   ALTER TABLE ONLY public.alunos ALTER COLUMN id SET DEFAULT nextval('public.alunos_id_seq'::regclass);
 8   ALTER TABLE public.alunos ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    218    217    218                      0    16507    alunos 
   TABLE DATA           6   COPY public.alunos (id, nome, cpf, turma) FROM stdin;
    public          postgres    false    218                     0    0    alunos_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.alunos_id_seq', 10, true);
          public          postgres    false    217            z           2606    16514    alunos alunos_cpf_key 
   CONSTRAINT     O   ALTER TABLE ONLY public.alunos
    ADD CONSTRAINT alunos_cpf_key UNIQUE (cpf);
 ?   ALTER TABLE ONLY public.alunos DROP CONSTRAINT alunos_cpf_key;
       public            postgres    false    218            |           2606    16512    alunos alunos_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.alunos
    ADD CONSTRAINT alunos_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.alunos DROP CONSTRAINT alunos_pkey;
       public            postgres    false    218               �   x�E�KN�0D�է�	Fq����ȖMC����5v��\��p1"���{ժ.	�YL�W�[w��U�v�0VRS����ę���l�.2�TCRx���85�|c�Pkj��>�k����(V��P�{=���^/�-�"�P�:<�#�1��BB�������xw�G̀B{4��[t7�M(t@ch�d�J�;�	��j�����{��n��ZC'"�B�[d     