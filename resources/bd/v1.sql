-- This script was generated by the ERD tool in pgAdmin 4.
-- Please log an issue at https://redmine.postgresql.org/projects/pgadmin4/issues/new if you find any bugs, including reproduction steps.
BEGIN;


CREATE TABLE IF NOT EXISTS public.accesibilidad
(
    id integer NOT NULL DEFAULT nextval('accesibilidad_id_seq'::regclass),
    tipo character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT accesibilidad_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.autoridad
(
    id integer NOT NULL DEFAULT nextval('autoridad_id_seq'::regclass),
    nombre text COLLATE pg_catalog."default" NOT NULL,
    institucion character varying(200) COLLATE pg_catalog."default" NOT NULL,
    cargo character varying(30) COLLATE pg_catalog."default" NOT NULL,
    ubicaciongeograficaid integer NOT NULL,
    CONSTRAINT autoridad_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.clasificacionpeligro
(
    id integer NOT NULL DEFAULT nextval('clasificacionpeligro_id_seq'::regclass),
    descripcion character varying(80) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT clasificacionpeligro_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.danosperdidas
(
    id integer NOT NULL DEFAULT nextval('danosperdidas_id_seq'::regclass),
    cantidad integer NOT NULL,
    costo integer NOT NULL,
    efectoid integer,
    descripcionid integer,
    CONSTRAINT danosperdidas_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.descripcion
(
    id integer NOT NULL DEFAULT nextval('descripcion_id_seq'::regclass),
    descripcionaccesibilidad text COLLATE pg_catalog."default",
    tipoinforme integer NOT NULL,
    descripcion text COLLATE pg_catalog."default" NOT NULL,
    poblacion integer,
    viviendas integer,
    establecimientosalud character varying(100) COLLATE pg_catalog."default",
    establecimientoeducativos character varying(100) COLLATE pg_catalog."default",
    actividadeconomica text COLLATE pg_catalog."default",
    serviciosbasicos text COLLATE pg_catalog."default",
    accionesestructurales text COLLATE pg_catalog."default",
    accionesnoestructurales text COLLATE pg_catalog."default",
    conclusiones text COLLATE pg_catalog."default",
    recomendaciones text COLLATE pg_catalog."default",
    accesibilidadid integer NOT NULL,
    CONSTRAINT descripcion_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.efecto
(
    id integer NOT NULL DEFAULT nextval('efecto_id_seq'::regclass),
    nombre text COLLATE pg_catalog."default" NOT NULL,
    unidad character varying(8) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT efecto_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.imagenes
(
    id integer NOT NULL DEFAULT nextval('imagenes_id_seq'::regclass),
    nombre character varying(100) COLLATE pg_catalog."default",
    descripcion text COLLATE pg_catalog."default" NOT NULL,
    urlimagen character varying(250) COLLATE pg_catalog."default" NOT NULL,
    fechasubida timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    descripcionid integer,
    CONSTRAINT imagenes_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.localidad
(
    id integer NOT NULL DEFAULT nextval('localidad_id_seq'::regclass),
    descripcion character varying(200) COLLATE pg_catalog."default" NOT NULL,
    altitud integer NOT NULL,
    latitud numeric(10, 6) NOT NULL,
    longitud numeric(10, 6) NOT NULL,
    utm character varying(3)[] COLLATE pg_catalog."default" NOT NULL,
    utmxi numeric(10, 5) NOT NULL,
    utmxf numeric(10, 5),
    utmyi numeric(10, 5) NOT NULL,
    utmyf numeric(10, 5),
    ubicaciongeograficaid integer NOT NULL,
    CONSTRAINT localidad_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.peligro
(
    id integer NOT NULL DEFAULT nextval('peligro_id_seq'::regclass),
    codsinpad integer NOT NULL,
    fechahora timestamp without time zone NOT NULL DEFAULT CURRENT_TIMESTAMP,
    tipopeligroid integer NOT NULL,
    localidadid integer NOT NULL,
    descripcionid integer NOT NULL,
    titularid integer NOT NULL,
    responsableid integer NOT NULL,
    CONSTRAINT peligro_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.tipopeligro
(
    id integer NOT NULL DEFAULT nextval('tipopeligro_id_seq'::regclass),
    tipo character varying(250) COLLATE pg_catalog."default" NOT NULL,
    clasificacionpeligroid integer NOT NULL,
    CONSTRAINT tipopeligro_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.ubicaciongeografica
(
    id integer NOT NULL DEFAULT nextval('ubicaciongeografica_id_seq'::regclass),
    departamento character varying(200) COLLATE pg_catalog."default" NOT NULL,
    provincia character varying(200) COLLATE pg_catalog."default" NOT NULL,
    distrito character varying(200) COLLATE pg_catalog."default" NOT NULL,
    ubigeo integer NOT NULL,
    CONSTRAINT ubicaciongeografica_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.usuario
(
    id integer NOT NULL DEFAULT nextval('usuario_id_seq'::regclass),
    nombres character varying(100) COLLATE pg_catalog."default" NOT NULL,
    apellidos character varying(100) COLLATE pg_catalog."default" NOT NULL,
    tipodocumento character varying(20) COLLATE pg_catalog."default" NOT NULL,
    numdocumento character varying(20) COLLATE pg_catalog."default" NOT NULL,
    direccion character varying(100) COLLATE pg_catalog."default",
    telefono character varying(20) COLLATE pg_catalog."default",
    email character varying(50) COLLATE pg_catalog."default" NOT NULL,
    cargo character varying(30) COLLATE pg_catalog."default",
    username character varying(20) COLLATE pg_catalog."default" NOT NULL,
    clave text COLLATE pg_catalog."default" NOT NULL,
    condicion integer,
    fechacreacion timestamp without time zone NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT usuario_pkey PRIMARY KEY (id),
    CONSTRAINT email UNIQUE (email),
    CONSTRAINT numdocumento UNIQUE (numdocumento),
    CONSTRAINT username UNIQUE (username)
);

CREATE TABLE IF NOT EXISTS public.permiso
(
    id integer NOT NULL,
    descripcion character varying,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.permisousuario
(
    id integer NOT NULL,
    idusuario integer NOT NULL,
    idpermiso integer NOT NULL,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.autoridad
    ADD CONSTRAINT "FK_AutoridadID_UbicacionGeograficaID" FOREIGN KEY (ubicaciongeograficaid)
    REFERENCES public.ubicaciongeografica (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE SET NULL
    NOT VALID;


ALTER TABLE IF EXISTS public.danosperdidas
    ADD CONSTRAINT "FK_DanosPerdidasID_DescripcionID" FOREIGN KEY (descripcionid)
    REFERENCES public.descripcion (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE SET NULL
    NOT VALID;


ALTER TABLE IF EXISTS public.danosperdidas
    ADD CONSTRAINT "FK_DanosPerdidasID_EfectoID" FOREIGN KEY (efectoid)
    REFERENCES public.efecto (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE SET NULL
    NOT VALID;


ALTER TABLE IF EXISTS public.descripcion
    ADD CONSTRAINT "FK_AccesibilidadID_DescripcionID" FOREIGN KEY (accesibilidadid)
    REFERENCES public.accesibilidad (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE SET NULL
    NOT VALID;


ALTER TABLE IF EXISTS public.imagenes
    ADD CONSTRAINT "FK_DescripcionID_ImagenesID" FOREIGN KEY (descripcionid)
    REFERENCES public.descripcion (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE SET NULL
    NOT VALID;


ALTER TABLE IF EXISTS public.localidad
    ADD CONSTRAINT "FK_Localidad_UbicacionGeograficaID" FOREIGN KEY (ubicaciongeograficaid)
    REFERENCES public.ubicaciongeografica (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE SET NULL
    NOT VALID;


ALTER TABLE IF EXISTS public.peligro
    ADD CONSTRAINT "FK_PeligroId_DescripcionID" FOREIGN KEY (descripcionid)
    REFERENCES public.descripcion (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE SET NULL
    NOT VALID;


ALTER TABLE IF EXISTS public.peligro
    ADD CONSTRAINT "FK_PeligroId_LocalidadID" FOREIGN KEY (localidadid)
    REFERENCES public.localidad (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE SET NULL
    NOT VALID;


ALTER TABLE IF EXISTS public.peligro
    ADD CONSTRAINT "FK_PeligroId_ResponsableID" FOREIGN KEY (responsableid)
    REFERENCES public.usuario (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE SET NULL
    NOT VALID;


ALTER TABLE IF EXISTS public.peligro
    ADD CONSTRAINT "FK_PeligroId_TipoPeligroID" FOREIGN KEY (tipopeligroid)
    REFERENCES public.tipopeligro (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE SET NULL
    NOT VALID;


ALTER TABLE IF EXISTS public.peligro
    ADD CONSTRAINT "FK_PeligroId_TitularID" FOREIGN KEY (titularid)
    REFERENCES public.usuario (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE SET NULL
    NOT VALID;


ALTER TABLE IF EXISTS public.tipopeligro
    ADD CONSTRAINT "FK_TipoPeligro_ClasificacionPeligro" FOREIGN KEY (clasificacionpeligroid)
    REFERENCES public.clasificacionpeligro (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE SET NULL
    NOT VALID;


ALTER TABLE IF EXISTS public.permisousuario
    ADD CONSTRAINT "FK_usuario_permisousuario" FOREIGN KEY (idusuario)
    REFERENCES public.usuario (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.permisousuario
    ADD CONSTRAINT "FK_permiso_permisousuario" FOREIGN KEY (idpermiso)
    REFERENCES public.permiso (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

END;