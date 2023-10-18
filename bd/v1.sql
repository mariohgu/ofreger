-- This script was generated by the ERD tool in pgAdmin 4.
-- Please log an issue at https://redmine.postgresql.org/projects/pgadmin4/issues/new if you find any bugs, including reproduction steps.
BEGIN;


CREATE TABLE IF NOT EXISTS public.UbicacionGeografica
(
    ID SERIAL NOT NULL,
    Departamento character varying(200) NOT NULL,
    Provincia character varying(200) NOT NULL,
    Distrito character varying(200) NOT NULL,
    Ubigeo integer NOT NULL,
    PRIMARY KEY (ID)
);

CREATE TABLE IF NOT EXISTS public.Localidad
(
    ID SERIAL NOT NULL,
    Descripcion character varying(200) NOT NULL,
    Altitud integer NOT NULL,
    Latitud numeric(10, 6) NOT NULL,
    Longitud numeric(10, 6) NOT NULL,
    UTM character varying(3)[] NOT NULL,
    UTMXI numeric(10, 5) NOT NULL,
    UTMXF numeric(10, 5),
    UTMYI numeric(10, 5) NOT NULL,
    UTMYF numeric(10, 5),
    UbicacionGeograficaID integer NOT NULL,
    PRIMARY KEY (ID)
);

CREATE TABLE IF NOT EXISTS public.ClasificacionPeligro
(
    ID SERIAL NOT NULL,
    Descripcion character varying(80) NOT NULL,
    PRIMARY KEY (ID)
);

CREATE TABLE IF NOT EXISTS public.TipoPeligro
(
    ID SERIAL NOT NULL,
    Tipo character varying(250) NOT NULL,
    ClasificacionPeligroID integer NOT NULL,
    PRIMARY KEY (ID)
);

CREATE TABLE IF NOT EXISTS public.Accesibilidad
(
    ID SERIAL NOT NULL,
    Tipo character varying(100) NOT NULL,
    PRIMARY KEY (ID)
);

CREATE TABLE IF NOT EXISTS public.Descripcion
(
    ID SERIAL NOT NULL,
    DescripcionAccesibilidad text,
    TipoInforme integer NOT NULL,
    Descripcion text NOT NULL,
    Poblacion integer,
    Viviendas integer,
    EstablecimientoSalud character varying(100),
    EstablecimientoEducativos character varying(100),
    ActividadEconomica text,
    ServiciosBasicos text,
    AccionesEstructurales text,
    AccionesNoEstructurales text,
    Conclusiones text,
    Recomendaciones text,
    AccesibilidadID integer NOT NULL,
    PRIMARY KEY (ID)
);

CREATE TABLE IF NOT EXISTS public.Autoridad
(
    ID SERIAL NOT NULL,
    Nombre text NOT NULL,
    Institucion character varying(200) NOT NULL,
    Cargo character varying(30) NOT NULL,
    UbicacionGeograficaID integer NOT NULL,
    PRIMARY KEY (ID)
);

CREATE TABLE IF NOT EXISTS public.Efecto
(
    ID SERIAL NOT NULL,
    Nombre text NOT NULL,
    Unidad character varying(8) NOT NULL,
    PRIMARY KEY (ID)
);

CREATE TABLE IF NOT EXISTS public.DanosPerdidas
(
    ID SERIAL NOT NULL,
    Cantidad integer NOT NULL,
    Costo integer NOT NULL,
    EfectoID integer,
    DescripcionID integer,
    PRIMARY KEY (ID)
);

CREATE TABLE IF NOT EXISTS public.Imagenes
(
    ID SERIAL NOT NULL,
    Nombre character varying(100),
    Descripcion text NOT NULL,
    UrlImagen character varying(250) NOT NULL,
    FechaSubida timestamp DEFAULT CURRENT_TIMESTAMP,
    DescripcionID integer,
    PRIMARY KEY (ID)
);

CREATE TABLE IF NOT EXISTS public.Usuario
(
    ID SERIAL NOT NULL,
    Nombres character varying(100) NOT NULL,
    Apellidos character varying(100) NOT NULL,
    TipoDocumento character varying(20) NOT NULL,
    NumDocumento character varying(20) NOT NULL,
    Direccion character varying(100),
    Telefono character varying(20),
    Email character varying(50) NOT NULL,
    Cargo character varying(30),
    Username character varying(20) NOT NULL,
    Clave text NOT NULL,
    Condicion integer,
    FechaCreacion timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (ID),
    CONSTRAINT NumDocumento UNIQUE (NumDocumento),
    CONSTRAINT Username UNIQUE (Username),
    CONSTRAINT Email UNIQUE (Email)
);

CREATE TABLE IF NOT EXISTS public.Peligro
(
    ID SERIAL NOT NULL,
    CodSinpad integer NOT NULL,
    FechaHora timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    TipoPeligroID integer NOT NULL,
    LocalidadID integer NOT NULL,
    DescripcionID integer NOT NULL,
    TitularID integer NOT NULL,
    ResponsableID integer NOT NULL,
    PRIMARY KEY (ID)
);

ALTER TABLE IF EXISTS public.Localidad
    ADD CONSTRAINT "FK_Localidad_UbicacionGeograficaID" FOREIGN KEY (UbicacionGeograficaID)
    REFERENCES public.UbicacionGeografica (ID) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE SET NULL
    NOT VALID;


ALTER TABLE IF EXISTS public.TipoPeligro
    ADD CONSTRAINT "FK_TipoPeligro_ClasificacionPeligro" FOREIGN KEY (ClasificacionPeligroID)
    REFERENCES public.ClasificacionPeligro (ID) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE SET NULL
    NOT VALID;


ALTER TABLE IF EXISTS public.Descripcion
    ADD CONSTRAINT "FK_AccesibilidadID_DescripcionID" FOREIGN KEY (AccesibilidadID)
    REFERENCES public.Accesibilidad (ID) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE SET NULL
    NOT VALID;


ALTER TABLE IF EXISTS public.Autoridad
    ADD CONSTRAINT "FK_AutoridadID_UbicacionGeograficaID" FOREIGN KEY (UbicacionGeograficaID)
    REFERENCES public.UbicacionGeografica (ID) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE SET NULL
    NOT VALID;


ALTER TABLE IF EXISTS public.DanosPerdidas
    ADD CONSTRAINT "FK_DanosPerdidasID_EfectoID" FOREIGN KEY (EfectoID)
    REFERENCES public.Efecto (ID) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE SET NULL
    NOT VALID;


ALTER TABLE IF EXISTS public.DanosPerdidas
    ADD CONSTRAINT "FK_DanosPerdidasID_DescripcionID" FOREIGN KEY (DescripcionID)
    REFERENCES public.Descripcion (ID) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE SET NULL
    NOT VALID;


ALTER TABLE IF EXISTS public.Imagenes
    ADD CONSTRAINT "FK_DescripcionID_ImagenesID" FOREIGN KEY (DescripcionID)
    REFERENCES public.Descripcion (ID) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE SET NULL
    NOT VALID;


ALTER TABLE IF EXISTS public.Peligro
    ADD CONSTRAINT "FK_PeligroId_TipoPeligroID" FOREIGN KEY (TipoPeligroID)
    REFERENCES public.TipoPeligro (ID) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE SET NULL
    NOT VALID;


ALTER TABLE IF EXISTS public.Peligro
    ADD CONSTRAINT "FK_PeligroId_LocalidadID" FOREIGN KEY (LocalidadID)
    REFERENCES public.Localidad (ID) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE SET NULL
    NOT VALID;


ALTER TABLE IF EXISTS public.Peligro
    ADD CONSTRAINT "FK_PeligroId_DescripcionID" FOREIGN KEY (DescripcionID)
    REFERENCES public.Descripcion (ID) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE SET NULL
    NOT VALID;


ALTER TABLE IF EXISTS public.Peligro
    ADD CONSTRAINT "FK_PeligroId_TitularID" FOREIGN KEY (TitularID)
    REFERENCES public.Usuario (ID) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE SET NULL
    NOT VALID;


ALTER TABLE IF EXISTS public.Peligro
    ADD CONSTRAINT "FK_PeligroId_ResponsableID" FOREIGN KEY (ResponsableID)
    REFERENCES public.Usuario (ID) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE SET NULL
    NOT VALID;

END;