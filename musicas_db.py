from sqlalchemy import and_, create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Artista(Base):
    __tablename__ = 'artista'

    id = Column(Integer, primary_key=True)
    nome = Column(String)

class Musica(Base):
    __tablename__ = 'musica'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    lingua = Column(String)
    genero = Column(String)

class ArtistaMusica(Base):
    __tablename__ = 'artista_musica'

    id = Column(Integer, primary_key=True)
    idArtista = Column(String)
    idMusica = Column(String)




def create_session():
    engine = create_engine('sqlite:///backupMusicas.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)
    return session

def record_musica(nome):
    musica = get_musica(name=nome)
    if (len(musica) == 0):
        session = create_session()
        registro = Musica()
        registro.nome = nome
        session.add(registro)
        session.commit()
        session.close()  
    if (len(musica) == 0):
        musica = get_musica(name=nome)
    id_musica = musica[0].id
    return id_musica

def record_artista(nome):
    artista = get_artista(name=nome)
    if (len(artista) == 0):
        session = create_session()
        registro = Artista()
        registro.nome = nome
        session.add(registro)
        session.commit()
        session.close()  
    if (len(artista) == 0):
        artista = get_artista(name=nome)
    id_artista = artista[0].id
    return id_artista

def record_artista_musica(id_artista, id_musica):
    artista_musica = get_artista_musica(id_artista=id_artista, id_musica=id_musica)
    if (len(artista_musica) == 0):
        session = create_session()
        registro = ArtistaMusica()
        registro.idArtista = id_artista
        registro.idMusica = id_musica
        session.add(registro)
        session.commit()
        session.close()  
    if (len(artista_musica) == 0):
        artista_musica = get_artista_musica(id_artista=id_artista, id_musica=id_musica)
    id_artista = artista_musica[0].id
    return id_artista

def get_artista_musica(id_artista=None, id_musica=None):
    session = create_session()
    filters = []
    if id_artista is not None:
        filters.append(ArtistaMusica.idArtista == id_artista)
    if id_musica is not None:
        filters.append(ArtistaMusica.idMusica == id_musica)
    resultados = session.query(ArtistaMusica).filter(and_(*filters)).all()
    session.close()

    return resultados

def get_artista(id=None, name=None):
    session = create_session()
    filters = []
    if id is not None:
        filters.append(Artista.id == id)
    if name is not None:
        filters.append(Artista.nome == name)
    resultados = session.query(Artista).filter(and_(*filters)).all()
    session.close()

    return resultados

def get_musica(id=None, name=None, language=None, genre=None):
    session = create_session()
    filters = []
    if id is not None:
        filters.append(Musica.id == id)
    if name is not None:
        filters.append(Musica.nome == name)
    if language is not None:
        filters.append(Musica.lingua == language)
    if genre is not None:
        filters.append(Musica.genero == genre)
    resultados = session.query(Musica).filter(and_(*filters)).all()
    session.close()

    return resultados