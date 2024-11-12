
from queue import Queue as Queue
from .Trainstation import Trainstation
from .SubwayLine import SubwayLine

class Controller:

    def __init__(self, id_controller=None, controller_number=None, subway_lines=None):
        self.id_controller = id_controller
        self.controller_number = controller_number
        self.subway_lines = subway_lines if subway_lines is not None else []
        self.path = []
        self.queue = Queue()

    # Getters
    def get_id_controller(self):
        return self.id_controller

    def get_controller_number(self):
        return self.controller_number

    def get_subway_lines(self):
        return self.subway_lines

    def get_queue(self):
        return self.queue

    # Setters
    def set_id_controller(self, id_controller):
        self.id_controller = id_controller
        return True

    def set_controller_number(self, controller_number):
        self.controller_number = controller_number
        return True

    def set_subway_lines(self, subway_lines):
        self.subway_lines = subway_lines
        return True

    def set_queue(self, queue):
        self.queue = queue
        return True

    def print_controller(self):
        print(f"Controller ID: {self.id_controller}, Number: {self.controller_number}")
        return True

    # Destructor
    def __del__(self):
        pass

    # General methods to the class
    def find_path(self, start: Trainstation, end: Trainstation):
    
        print(f"Finding path from {start.get_id()} to {end.get_id()}")
    
        # Si las estaciones no son nulas
        if start is None or end is None:
            print("Error: Invalid TrainStation")
            return None

        # Si las estaciones son validas
        # se agrega start a la cola

        # Inicializa la cola y marca la estación inicial como visitada
        self.queue.put(start)
        start.set_visited_state(True)

        # bucle externo: mientras la cola no este vacia se revisan los vecinos
        while not self.queue.empty():
            current = self.queue.get()  # se obtiene el primer elemento de la cola

            if current == end:
                # si se llega a la estación final se imprime el camino
                at = end
                while at is not None:
                    self.path.append(at)
                    at = at.get_predecessor()

                self.reset_visited_state()
                return self.path

            else:
                # si no se llega a la estación final se agregan los vecinos a la cola
                neighbors = current.get_neighbors()

                for neighbor in neighbors:
                    if not neighbor.get_visited_state():
                        self.queue.put(neighbor)
                        neighbor.set_visited_state(True)
                        neighbor.set_predecessor(current)

        # Si las estaciones son validas -> END
        self.reset_visited_state()

        # if the path is not found
        print("\n---> Path not found <---\n")
        return None

    def find_node(self, name: str):

        start = self.get_subway_lines()[0].get_terminal_a()

        # Inicializa la cola y marca la estación inicial como visitada
        self.queue.put(start)
        start.set_visited_state(True)

        # bucle externo: mientras la cola no este vacia se revisan los vecinos
        while not self.queue.empty():
            current = self.queue.get()  # se obtiene el primer elemento de la cola

            if current.get_id() == name:
                self.reset_visited_state()
                return current

            else:
                # se obtiene el primer vecino (neighbor) del nodo que se saco de la cola (current)
                neighbors = current.get_neighbors()

                # se revisa la lista de vecinos de current
                for neighbor in neighbors:
                    if neighbor.get_neighbors() and not neighbor.get_visited_state():
                        self.queue.put(neighbor)
                        neighbor.set_visited_state(True)


        # if the path is not found
        self.reset_visited_state()
        print("\n---> No se encontró el nodo <---\n")

        return None

    def reset_visited_state(self):

        start = self.get_subway_lines()[0].get_terminal_a()
        self.queue.put(start)
        start.set_visited_state(True)

        # bucle externo: mientras la cola no este vacia se revisan los vecinos
        while not self.queue.empty():
            current = self.queue.get()  # se obtiene el primer elemento de la cola
            current.set_visited_state(False)

            neighbors = current.get_neighbors()

            # se revisa la lista de vecinos de neighbor
            for neighbor in neighbors:
                neighbor_station = neighbor

                if neighbor_station.get_neighbors() and neighbor_station.get_visited_state():
                    neighbor_station.set_visited_state(False)
                    self.queue.put(neighbor_station)

        print("Se reinicio el estado de los nodos")

    def initialize_data(self):
        
        # Creación de estaciones

        # Estaciones de transbordo

        # Línea 1
        Tacubaya = Trainstation("Tacubaya")
        Balderas = Trainstation("Balderas")
        SaltoDelAgua = Trainstation("Salto del Agua")
        PinoSuarez = Trainstation("Pino Suárez")
        Candelaria = Trainstation("Candelaria")
        SanLazaro = Trainstation("San Lázaro")
        Pantitlan = Trainstation("Pantitlán")

        # Línea 2
        Tacuba = Trainstation("Tacuba")
        Hidalgo = Trainstation("Hidalgo")
        BellasArtes = Trainstation("Bellas Artes")
        Chabacano = Trainstation("Chabacano")
        Ermita = Trainstation("Ermita")

        # Línea 3
        D18deMarzo = Trainstation("18 de Marzo")
        LaRaza = Trainstation("La Raza")
        Guerrero = Trainstation("Guerrero")
        CentroMedico = Trainstation("Centro Médico")
        Zapata = Trainstation("Zapata")

        # Línea 4
        MartinCarrera = Trainstation("Martín Carrera")
        Consulado = Trainstation("Consulado")
        Morelos = Trainstation("Morelos")
        Jamaica = Trainstation("Jamaica")
        SantaAnita = Trainstation("Santa Anita")

        # Línea 5
        InstitutoDelPetroleo = Trainstation("Instituto del Petróleo")
        Oceania = Trainstation("Oceanía")

        # Línea 6
        ElRosario = Trainstation("El Rosario")

        # Línea 7
        Mixcoac = Trainstation("Mixcoac")

        # Línea 8
        Garibaldi = Trainstation("Garibaldi")
        Atlalilco = Trainstation("Atlalilco")

        # Las siguientes líneas se dejan vacías porque sus respectivas estaciones
        # de transbordo se encuentran en otras líneas

        # Línea 9

        # Línea A

        # Línea B

        # Línea 12

        # Estaciones sin transbordo

        # Línea 1
        Observatorio = Trainstation("Observatorio")
        Juanacatlan = Trainstation("Juanacatlán")
        Chapultepec = Trainstation("Chapultepec")
        Sevilla = Trainstation("Sevilla")
        Insurgentes = Trainstation("Insurgentes")
        Cuauhtemoc = Trainstation("Cuauhtémoc")
        SanjuanDeLetran = Trainstation("San Juan de Letrán")
        Merced = Trainstation("Merced")
        Moctezuma = Trainstation("Moctezuma")
        Balbuena = Trainstation("Balbuena")
        BoulevardPuertoAereo = Trainstation("Boulevard Puerto Aéreo")
        GomezFarias = Trainstation("Gómez Farías")
        Zaragoza = Trainstation("Zaragoza")
        Isabelcatolica = Trainstation("Isabel la Católica")
        
        # Línea 2
        CuatroCaminos = Trainstation("Cuatro Caminos")
        Panteones = Trainstation("Panteones")
        Cuitlahuac = Trainstation("Cuitláhuac")
        Popotla = Trainstation("Popotla")
        ColegioMilitar = Trainstation("Colegio Militar")
        Normal = Trainstation("Normal")
        SanCosme = Trainstation("San Cosme")
        Revolucion = Trainstation("Revolución")
        Allende = Trainstation("Allende")
        Zocalo = Trainstation("Zócalo")
        SanAntonioAbad = Trainstation("San Antonio Abad")
        Viaducto = Trainstation("Viaducto")
        Xola = Trainstation("Xola")
        VillaDeCortes = Trainstation("Villa de Cortés")
        Nativitas = Trainstation("Nativitas")
        Portales = Trainstation("Portales")
        GeneralAnaya = Trainstation("General Anaya")
        Tasqueña = Trainstation("Tasqueña")
        
        # Línea 3
        IndiosVerdes = Trainstation("Indios Verdes")
        Potrero = Trainstation("Potrero")
        Tlatelolco = Trainstation("Tlatelolco")
        Juarez = Trainstation("Juárez")
        NinosHeroes = Trainstation("Niños Héroes")
        HospitalGeneral = Trainstation("Hospital General")
        Etiopia = Trainstation("Etiopía")
        Eugenia = Trainstation("Eugenia")
        DivisionDelNorte = Trainstation("División del Norte")
        Coyoacan = Trainstation("Coyoacán")
        Viveros = Trainstation("Viveros")
        MiguelAngelDeQuevedo = Trainstation("Miguel Ángel de Quevedo")
        Copilco = Trainstation("Copilco")
        Universidad = Trainstation("Universidad")
        
        # Línea 4
        Talisman = Trainstation("Talismán")
        Bondojito = Trainstation("Bondojito")
        CanalDelNorte = Trainstation("Canal del Norte")
        FrayServando = Trainstation("Fray Servando")
        
        # Línea 5
        Hangares = Trainstation("Hangares")
        TerminalAerea = Trainstation("Terminal Aérea")
        Aragon = Trainstation("Aragón")
        EduardoMolina = Trainstation("Eduardo Molina")
        ValleGomez = Trainstation("Valle Gómez")
        Misterios = Trainstation("Misterios")
        AutobusesDelNorte = Trainstation("Autobuses del Norte")
        Politecnico = Trainstation("Politécnico")
        
        # Línea 6
        Tezozomoc = Trainstation("Tezozómoc")
        UAMAzcapotzalco = Trainstation("UAM-Azcapotzalco")
        Ferrería = Trainstation("Ferrería")
        Norte45 = Trainstation("Norte 45")
        Vallejo = Trainstation("Vallejo")
        Lindavista = Trainstation("Lindavista")
        LaVillaBasilica = Trainstation("La Villa-Basílica")
        
        # Línea 7
        AquilesSerdan = Trainstation("Aquiles Serdán")
        Camarones = Trainstation("Camarones")
        Refineria = Trainstation("Refinería")
        SanJoaquin = Trainstation("San Joaquín")
        Polanco = Trainstation("Polanco")
        Auditorio = Trainstation("Auditorio")
        Constituyentes = Trainstation("Constituyentes")
        SanPedroDeLosPinos = Trainstation("San Pedro de los Pinos")
        SanAntonio = Trainstation("San Antonio")
        BarrancaDelMuerto = Trainstation("Barranca del Muerto")
        
        # Línea 8
        SanjuanDeLetran = Trainstation("San Juan de Letrán")
        Doctores = Trainstation("Doctores")
        Obrera = Trainstation("Obrera")
        LaViga = Trainstation("La Viga")
        Coyuya = Trainstation("Coyuya")
        Iztacalco = Trainstation("Iztacalco")
        Apatlaco = Trainstation("Apatlaco")
        Aculco = Trainstation("Aculco")
        Escuadron201 = Trainstation("Escuadrón 201")
        Iztapalapa = Trainstation("Iztapalapa")
        CerroDeLaEstrella = Trainstation("Cerro de la Estrella")
        UAM = Trainstation("UAM")
        ConstitucionDe1917 = Trainstation("Constitución de 1917")
        
        # Línea 9
        Puebla = Trainstation("Puebla")
        CiudadDeportiva = Trainstation("Ciudad Deportiva")
        Velodromo = Trainstation("Velódromo")
        Mixiuhca = Trainstation("Mixiuhca")
        LazaroCardenas = Trainstation("Lázaro Cárdenas")
        Chilpancingo = Trainstation("Chilpancingo")
        Patriotismo = Trainstation("Patriotismo")
        
        # Línea A
        AgricolaOriental = Trainstation("Agrícola Oriental")
        CanalDeSanJuan = Trainstation("Canal de San Juan")
        Tepalcates = Trainstation("Tepalcates")
        Guelatao = Trainstation("Guelatao")
        PenonViejo = Trainstation("Peñón Viejo")
        Acatitla = Trainstation("Acatitla")
        SantaMarta = Trainstation("Santa Marta")
        LosReyes = Trainstation("Los Reyes")
        LaPaz = Trainstation("La Paz")
        
        # Línea B
        Buenavista = Trainstation("Buenavista")
        Lagunilla = Trainstation("Lagunilla")
        Tepito = Trainstation("Tepito")
        RicardoFloresMagon = Trainstation("Ricardo Flores Magón")
        RomeroRubio = Trainstation("Romero Rubio")
        DeportivoOceania = Trainstation("Deportivo Oceanía")
        VillaDeAragon = Trainstation("Villa de Aragón")
        BosqueDeAragon = Trainstation("Bosque de Aragón")
        Nezahualcoyotl = Trainstation("Nezahualcoyotl")
        Impulsora = Trainstation("Impulsora")
        RioDeLosRemedios = Trainstation("Rio De Los Remedios")
        Muzquiz = Trainstation("Muzquiz")
        Ecatepec = Trainstation("Ecatepec")
        Olimpica = Trainstation("Olimpica")
        PlazaAragon = Trainstation("Plaza Aragon")
        CiudadAzteca = Trainstation("Ciudad Azteca")
        
        # Línea 12
        InsurgentesSur = Trainstation("Insurgentes Sur")
        Hospital20DeNoviembre = Trainstation("Hospital 20 de Noviembre")
        ParqueDeLosVenados = Trainstation("Parque de los Venados")
        EjeCentral = Trainstation("Eje Central")
        Mexicaltzingo = Trainstation("Mexicaltzingo")
        Culhuacan = Trainstation("Culhuacán")
        SanAndresTomatlan = Trainstation("San Andrés Tomatlán")
        LomasEstrella = Trainstation("Lomas Estrella")
        Calle11 = Trainstation("Calle 11")
        PerifericoOriente = Trainstation("Periférico Oriente")
        Tezonco = Trainstation("Tezonco")
        Olivos = Trainstation("Olivos")
        Nopalera = Trainstation("Nopalera")
        Zapotitlan = Trainstation("Zapotitlán")
        Tlaltenco = Trainstation("Tlaltenco")
        Tlahuac = Trainstation("Tláhuac")
                
        # Creación de la conexión entre estaciones

        # Línea 1
        Observatorio.addNeighbor(Tacubaya)
        Tacubaya.addNeighbor(Observatorio)
        Tacubaya.addNeighbor(Juanacatlan)
        Juanacatlan.addNeighbor(Tacubaya)
        Juanacatlan.addNeighbor(Chapultepec)
        Chapultepec.addNeighbor(Juanacatlan)
        Chapultepec.addNeighbor(Sevilla)
        Sevilla.addNeighbor(Chapultepec)
        Sevilla.addNeighbor(Insurgentes)
        Insurgentes.addNeighbor(Sevilla)
        Insurgentes.addNeighbor(Cuauhtemoc)
        Cuauhtemoc.addNeighbor(Insurgentes)
        Cuauhtemoc.addNeighbor(Balderas)
        Balderas.addNeighbor(Cuauhtemoc)
        Balderas.addNeighbor(SaltoDelAgua)
        SaltoDelAgua.addNeighbor(Balderas)
        SaltoDelAgua.addNeighbor(Isabelcatolica)
        Isabelcatolica.addNeighbor(SaltoDelAgua)
        Isabelcatolica.addNeighbor(PinoSuarez)
        PinoSuarez.addNeighbor(Isabelcatolica)
        PinoSuarez.addNeighbor(Merced)
        Merced.addNeighbor(PinoSuarez)
        Merced.addNeighbor(Candelaria)
        Candelaria.addNeighbor(Merced)
        Candelaria.addNeighbor(SanLazaro)
        SanLazaro.addNeighbor(Candelaria)
        SanLazaro.addNeighbor(Moctezuma)
        Moctezuma.addNeighbor(SanLazaro)
        Moctezuma.addNeighbor(Balbuena)
        Balbuena.addNeighbor(Moctezuma)
        Balbuena.addNeighbor(BoulevardPuertoAereo)
        BoulevardPuertoAereo.addNeighbor(Balbuena)
        BoulevardPuertoAereo.addNeighbor(GomezFarias)
        GomezFarias.addNeighbor(BoulevardPuertoAereo)
        GomezFarias.addNeighbor(Zaragoza)
        Zaragoza.addNeighbor(GomezFarias)
        Zaragoza.addNeighbor(Pantitlan)
        Pantitlan.addNeighbor(Zaragoza)

        # Línea 2
        CuatroCaminos.addNeighbor(Panteones)
        Panteones.addNeighbor(CuatroCaminos)
        Panteones.addNeighbor(Tacuba)
        Tacuba.addNeighbor(Panteones)
        Tacuba.addNeighbor(Cuitlahuac)
        Cuitlahuac.addNeighbor(Tacuba)
        Cuitlahuac.addNeighbor(Popotla)
        Popotla.addNeighbor(Cuitlahuac)
        Popotla.addNeighbor(ColegioMilitar)
        ColegioMilitar.addNeighbor(Popotla)
        ColegioMilitar.addNeighbor(Normal)
        Normal.addNeighbor(ColegioMilitar)
        Normal.addNeighbor(SanCosme)
        SanCosme.addNeighbor(Normal)
        SanCosme.addNeighbor(Revolucion)
        Revolucion.addNeighbor(SanCosme)
        Revolucion.addNeighbor(Hidalgo)
        Hidalgo.addNeighbor(Revolucion)
        Hidalgo.addNeighbor(BellasArtes)
        BellasArtes.addNeighbor(Hidalgo)
        BellasArtes.addNeighbor(Allende)
        Allende.addNeighbor(BellasArtes)
        Allende.addNeighbor(Zocalo)
        Zocalo.addNeighbor(Allende)
        Zocalo.addNeighbor(PinoSuarez)
        PinoSuarez.addNeighbor(Zocalo)
        PinoSuarez.addNeighbor(SanAntonioAbad)
        SanAntonioAbad.addNeighbor(PinoSuarez)
        SanAntonioAbad.addNeighbor(Chabacano)
        Chabacano.addNeighbor(SanAntonioAbad)
        Chabacano.addNeighbor(Viaducto)
        Viaducto.addNeighbor(Chabacano)
        Viaducto.addNeighbor(Xola)
        Xola.addNeighbor(Viaducto)
        Xola.addNeighbor(VillaDeCortes)
        VillaDeCortes.addNeighbor(Xola)
        VillaDeCortes.addNeighbor(Nativitas)
        Nativitas.addNeighbor(VillaDeCortes)
        Nativitas.addNeighbor(Portales)
        Portales.addNeighbor(Nativitas)
        Portales.addNeighbor(Ermita)
        Ermita.addNeighbor(Portales)
        Ermita.addNeighbor(GeneralAnaya)
        GeneralAnaya.addNeighbor(Ermita)
        GeneralAnaya.addNeighbor(Tasqueña)
        Tasqueña.addNeighbor(GeneralAnaya)

        # Línea 3
        IndiosVerdes.addNeighbor(D18deMarzo)
        D18deMarzo.addNeighbor(IndiosVerdes)
        D18deMarzo.addNeighbor(Potrero)
        Potrero.addNeighbor(D18deMarzo)
        Potrero.addNeighbor(LaRaza)
        LaRaza.addNeighbor(Potrero)
        LaRaza.addNeighbor(Tlatelolco)
        Tlatelolco.addNeighbor(LaRaza)
        Tlatelolco.addNeighbor(Guerrero)
        Guerrero.addNeighbor(Tlatelolco)
        Guerrero.addNeighbor(Hidalgo)
        Hidalgo.addNeighbor(Guerrero)
        Hidalgo.addNeighbor(Juarez)
        Juarez.addNeighbor(Hidalgo)
        Juarez.addNeighbor(Balderas)
        Balderas.addNeighbor(Juarez)
        Balderas.addNeighbor(NinosHeroes)
        NinosHeroes.addNeighbor(Balderas)
        NinosHeroes.addNeighbor(HospitalGeneral)
        HospitalGeneral.addNeighbor(NinosHeroes)
        HospitalGeneral.addNeighbor(CentroMedico)
        CentroMedico.addNeighbor(HospitalGeneral)
        CentroMedico.addNeighbor(Etiopia)
        Etiopia.addNeighbor(CentroMedico)
        Etiopia.addNeighbor(Eugenia)
        Eugenia.addNeighbor(Etiopia)
        Eugenia.addNeighbor(DivisionDelNorte)
        DivisionDelNorte.addNeighbor(Eugenia)
        DivisionDelNorte.addNeighbor(Zapata)
        Zapata.addNeighbor(DivisionDelNorte)
        Zapata.addNeighbor(Coyoacan)
        Coyoacan.addNeighbor(Zapata)
        Coyoacan.addNeighbor(Viveros)
        Viveros.addNeighbor(Coyoacan)
        Viveros.addNeighbor(MiguelAngelDeQuevedo)
        MiguelAngelDeQuevedo.addNeighbor(Viveros)
        MiguelAngelDeQuevedo.addNeighbor(Copilco)
        Copilco.addNeighbor(MiguelAngelDeQuevedo)
        Copilco.addNeighbor(Universidad)
        Universidad.addNeighbor(Copilco)

        # Línea 4
        MartinCarrera.addNeighbor(Talisman)
        Talisman.addNeighbor(MartinCarrera)
        Talisman.addNeighbor(Bondojito)
        Bondojito.addNeighbor(Talisman)
        Bondojito.addNeighbor(Consulado)
        Consulado.addNeighbor(Bondojito)
        Consulado.addNeighbor(CanalDelNorte)
        CanalDelNorte.addNeighbor(Consulado)
        CanalDelNorte.addNeighbor(Morelos)
        Morelos.addNeighbor(CanalDelNorte)
        Morelos.addNeighbor(Candelaria)
        Candelaria.addNeighbor(Morelos)
        Candelaria.addNeighbor(FrayServando)
        FrayServando.addNeighbor(Candelaria)
        FrayServando.addNeighbor(Jamaica)
        Jamaica.addNeighbor(FrayServando)
        Jamaica.addNeighbor(SantaAnita)
        SantaAnita.addNeighbor(Jamaica)

        # Línea 5
        Politecnico.addNeighbor(InstitutoDelPetroleo)
        InstitutoDelPetroleo.addNeighbor(Politecnico)
        InstitutoDelPetroleo.addNeighbor(AutobusesDelNorte)
        AutobusesDelNorte.addNeighbor(InstitutoDelPetroleo)
        AutobusesDelNorte.addNeighbor(LaRaza)
        LaRaza.addNeighbor(AutobusesDelNorte)
        LaRaza.addNeighbor(Misterios)
        Misterios.addNeighbor(LaRaza)
        Misterios.addNeighbor(ValleGomez)
        ValleGomez.addNeighbor(Misterios)
        ValleGomez.addNeighbor(Consulado)
        Consulado.addNeighbor(ValleGomez)
        Consulado.addNeighbor(EduardoMolina)
        EduardoMolina.addNeighbor(Consulado)
        EduardoMolina.addNeighbor(Aragon)
        Aragon.addNeighbor(EduardoMolina)
        Aragon.addNeighbor(Oceania)
        Oceania.addNeighbor(Aragon)
        Oceania.addNeighbor(TerminalAerea)
        TerminalAerea.addNeighbor(Oceania)
        TerminalAerea.addNeighbor(Hangares)
        Hangares.addNeighbor(TerminalAerea)
        Hangares.addNeighbor(Pantitlan)
        Pantitlan.addNeighbor(Hangares)

        # Línea 6
        ElRosario.addNeighbor(Tezozomoc)
        Tezozomoc.addNeighbor(ElRosario)
        Tezozomoc.addNeighbor(UAMAzcapotzalco)
        UAMAzcapotzalco.addNeighbor(Tezozomoc)
        UAMAzcapotzalco.addNeighbor(Ferrería)
        Ferrería.addNeighbor(UAMAzcapotzalco)
        Ferrería.addNeighbor(Norte45)
        Norte45.addNeighbor(Ferrería)
        Norte45.addNeighbor(Vallejo)
        Vallejo.addNeighbor(Norte45)
        Vallejo.addNeighbor(InstitutoDelPetroleo)
        InstitutoDelPetroleo.addNeighbor(Vallejo)
        InstitutoDelPetroleo.addNeighbor(Lindavista)
        Lindavista.addNeighbor(InstitutoDelPetroleo)
        Lindavista.addNeighbor(D18deMarzo)
        D18deMarzo.addNeighbor(Lindavista)
        D18deMarzo.addNeighbor(LaVillaBasilica)
        LaVillaBasilica.addNeighbor(D18deMarzo)
        LaVillaBasilica.addNeighbor(MartinCarrera)
        MartinCarrera.addNeighbor(LaVillaBasilica)

        # Línea 7
        ElRosario.addNeighbor(AquilesSerdan)
        AquilesSerdan.addNeighbor(ElRosario)
        AquilesSerdan.addNeighbor(Camarones)
        Camarones.addNeighbor(AquilesSerdan)
        Camarones.addNeighbor(Refineria)
        Refineria.addNeighbor(Camarones)
        Refineria.addNeighbor(Tacuba)
        Tacuba.addNeighbor(Refineria)
        Tacuba.addNeighbor(SanJoaquin)
        SanJoaquin.addNeighbor(Tacuba)
        SanJoaquin.addNeighbor(Polanco)
        Polanco.addNeighbor(SanJoaquin)
        Polanco.addNeighbor(Auditorio)
        Auditorio.addNeighbor(Polanco)
        Auditorio.addNeighbor(Constituyentes)
        Constituyentes.addNeighbor(Auditorio)
        Constituyentes.addNeighbor(Tacubaya)
        Tacubaya.addNeighbor(Constituyentes)
        Tacubaya.addNeighbor(SanPedroDeLosPinos)
        SanPedroDeLosPinos.addNeighbor(Tacubaya)
        SanPedroDeLosPinos.addNeighbor(SanAntonio)
        SanAntonio.addNeighbor(SanPedroDeLosPinos)
        SanAntonio.addNeighbor(Mixcoac)
        Mixcoac.addNeighbor(SanAntonio)
        Mixcoac.addNeighbor(BarrancaDelMuerto)
        BarrancaDelMuerto.addNeighbor(Mixcoac)

        # Línea 8
        Garibaldi.addNeighbor(BellasArtes)
        BellasArtes.addNeighbor(Garibaldi)
        BellasArtes.addNeighbor(SanjuanDeLetran)
        SanjuanDeLetran.addNeighbor(BellasArtes)
        SanjuanDeLetran.addNeighbor(SaltoDelAgua)
        SaltoDelAgua.addNeighbor(SanjuanDeLetran)
        SaltoDelAgua.addNeighbor(Doctores)
        Doctores.addNeighbor(SaltoDelAgua)
        Doctores.addNeighbor(Obrera)
        Obrera.addNeighbor(Doctores)
        Obrera.addNeighbor(Chabacano)
        Chabacano.addNeighbor(Obrera)
        Chabacano.addNeighbor(LaViga)
        LaViga.addNeighbor(Chabacano)
        LaViga.addNeighbor(SantaAnita)
        SantaAnita.addNeighbor(LaViga)
        SantaAnita.addNeighbor(Coyuya)
        Coyuya.addNeighbor(SantaAnita)
        Coyuya.addNeighbor(Iztacalco)
        Iztacalco.addNeighbor(Coyuya)
        Iztacalco.addNeighbor(Apatlaco)
        Apatlaco.addNeighbor(Iztacalco)
        Apatlaco.addNeighbor(Aculco)
        Aculco.addNeighbor(Apatlaco)
        Aculco.addNeighbor(Escuadron201)
        Escuadron201.addNeighbor(Aculco)
        Escuadron201.addNeighbor(Atlalilco)
        Atlalilco.addNeighbor(Escuadron201)
        Atlalilco.addNeighbor(Iztapalapa)
        Iztapalapa.addNeighbor(Atlalilco)
        Iztapalapa.addNeighbor(CerroDeLaEstrella)
        CerroDeLaEstrella.addNeighbor(Iztapalapa)
        CerroDeLaEstrella.addNeighbor(UAM)
        UAM.addNeighbor(CerroDeLaEstrella)
        UAM.addNeighbor(ConstitucionDe1917)
        ConstitucionDe1917.addNeighbor(UAM)

        # Línea 9
        Tacubaya.addNeighbor(Patriotismo)
        Patriotismo.addNeighbor(Tacubaya)
        Patriotismo.addNeighbor(Chilpancingo)
        Chilpancingo.addNeighbor(Patriotismo)
        Chilpancingo.addNeighbor(CentroMedico)
        CentroMedico.addNeighbor(Chilpancingo)
        CentroMedico.addNeighbor(LazaroCardenas)
        LazaroCardenas.addNeighbor(CentroMedico)
        LazaroCardenas.addNeighbor(Chabacano)
        Chabacano.addNeighbor(LazaroCardenas)
        Chabacano.addNeighbor(Jamaica)
        Jamaica.addNeighbor(Chabacano)
        Jamaica.addNeighbor(Mixiuhca)
        Mixiuhca.addNeighbor(Jamaica)
        Mixiuhca.addNeighbor(Velodromo)
        Velodromo.addNeighbor(Mixiuhca)
        Velodromo.addNeighbor(CiudadDeportiva)
        CiudadDeportiva.addNeighbor(Velodromo)
        CiudadDeportiva.addNeighbor(Puebla)
        Puebla.addNeighbor(CiudadDeportiva)
        Puebla.addNeighbor(Pantitlan)
        Pantitlan.addNeighbor(Puebla)

        # Línea A
        Pantitlan.addNeighbor(AgricolaOriental)
        AgricolaOriental.addNeighbor(Pantitlan)
        AgricolaOriental.addNeighbor(CanalDeSanJuan)
        CanalDeSanJuan.addNeighbor(AgricolaOriental)
        CanalDeSanJuan.addNeighbor(Tepalcates)
        Tepalcates.addNeighbor(CanalDeSanJuan)
        Tepalcates.addNeighbor(Guelatao)
        Guelatao.addNeighbor(Tepalcates)
        Guelatao.addNeighbor(PenonViejo)
        PenonViejo.addNeighbor(Guelatao)
        PenonViejo.addNeighbor(Acatitla)
        Acatitla.addNeighbor(PenonViejo)
        Acatitla.addNeighbor(SantaMarta)
        SantaMarta.addNeighbor(Acatitla)
        SantaMarta.addNeighbor(LosReyes)
        LosReyes.addNeighbor(SantaMarta)
        LosReyes.addNeighbor(LaPaz)
        LaPaz.addNeighbor(LosReyes)

        # Línea B
        Buenavista.addNeighbor(Guerrero)
        Guerrero.addNeighbor(Buenavista)
        Guerrero.addNeighbor(Garibaldi)
        Garibaldi.addNeighbor(Guerrero)
        Garibaldi.addNeighbor(Lagunilla)
        Lagunilla.addNeighbor(Garibaldi)
        Lagunilla.addNeighbor(Tepito)
        Tepito.addNeighbor(Lagunilla)
        Tepito.addNeighbor(Morelos)
        Morelos.addNeighbor(Tepito)
        Morelos.addNeighbor(SanLazaro)
        SanLazaro.addNeighbor(Morelos)
        SanLazaro.addNeighbor(RicardoFloresMagon)
        RicardoFloresMagon.addNeighbor(SanLazaro)
        RicardoFloresMagon.addNeighbor(RomeroRubio)
        RomeroRubio.addNeighbor(RicardoFloresMagon)
        RomeroRubio.addNeighbor(DeportivoOceania)
        DeportivoOceania.addNeighbor(RomeroRubio)
        DeportivoOceania.addNeighbor(VillaDeAragon)
        VillaDeAragon.addNeighbor(DeportivoOceania)
        VillaDeAragon.addNeighbor(BosqueDeAragon)
        BosqueDeAragon.addNeighbor(VillaDeAragon)
        BosqueDeAragon.addNeighbor(Nezahualcoyotl)
        Nezahualcoyotl.addNeighbor(BosqueDeAragon)
        Nezahualcoyotl.addNeighbor(Impulsora)
        Impulsora.addNeighbor(Nezahualcoyotl)
        Impulsora.addNeighbor(RioDeLosRemedios)
        RioDeLosRemedios.addNeighbor(Impulsora)
        RioDeLosRemedios.addNeighbor(Muzquiz)
        Muzquiz.addNeighbor(RioDeLosRemedios)
        Muzquiz.addNeighbor(Ecatepec)
        Ecatepec.addNeighbor(Muzquiz)
        Ecatepec.addNeighbor(Olimpica)
        Olimpica.addNeighbor(Ecatepec)
        Olimpica.addNeighbor(PlazaAragon)
        PlazaAragon.addNeighbor(Olimpica)
        PlazaAragon.addNeighbor(CiudadAzteca)
        CiudadAzteca.addNeighbor(PlazaAragon)

        # Línea 12
        Mixcoac.addNeighbor(InsurgentesSur)
        InsurgentesSur.addNeighbor(Mixcoac)
        InsurgentesSur.addNeighbor(Hospital20DeNoviembre)
        Hospital20DeNoviembre.addNeighbor(InsurgentesSur)
        Hospital20DeNoviembre.addNeighbor(Zapata)
        Zapata.addNeighbor(Hospital20DeNoviembre)
        Zapata.addNeighbor(ParqueDeLosVenados)
        ParqueDeLosVenados.addNeighbor(Zapata)
        ParqueDeLosVenados.addNeighbor(EjeCentral)
        EjeCentral.addNeighbor(ParqueDeLosVenados)
        EjeCentral.addNeighbor(Ermita)
        Ermita.addNeighbor(EjeCentral)
        Ermita.addNeighbor(Mexicaltzingo)
        Mexicaltzingo.addNeighbor(Ermita)
        Mexicaltzingo.addNeighbor(Atlalilco)
        Atlalilco.addNeighbor(Mexicaltzingo)
        Atlalilco.addNeighbor(Culhuacan)
        Culhuacan.addNeighbor(Atlalilco)
        Culhuacan.addNeighbor(SanAndresTomatlan)
        SanAndresTomatlan.addNeighbor(Culhuacan)
        SanAndresTomatlan.addNeighbor(LomasEstrella)
        LomasEstrella.addNeighbor(SanAndresTomatlan)
        LomasEstrella.addNeighbor(Calle11)
        Calle11.addNeighbor(LomasEstrella)
        Calle11.addNeighbor(PerifericoOriente)
        PerifericoOriente.addNeighbor(Calle11)
        PerifericoOriente.addNeighbor(Tezonco)
        Tezonco.addNeighbor(PerifericoOriente)
        Tezonco.addNeighbor(Olivos)
        Olivos.addNeighbor(Tezonco)
        Olivos.addNeighbor(Nopalera)
        Nopalera.addNeighbor(Olivos)
        Nopalera.addNeighbor(Zapotitlan)
        Zapotitlan.addNeighbor(Nopalera)
        Zapotitlan.addNeighbor(Tlaltenco)
        Tlaltenco.addNeighbor(Zapotitlan)
        Tlaltenco.addNeighbor(Tlahuac)
        Tlahuac.addNeighbor(Tlaltenco)

        L1 = SubwayLine("Línea 1", "L1", Observatorio, Pantitlan)
        L2 = SubwayLine("Línea 2", "L2", CuatroCaminos, Tasqueña)
        L3 = SubwayLine("Línea 3", "L3", IndiosVerdes, Universidad)
        L4 = SubwayLine("Línea 4", "L4", MartinCarrera, SantaAnita)
        L5 = SubwayLine("Línea 5", "L5", Politecnico, Pantitlan)
        L6 = SubwayLine("Línea 6", "L6", ElRosario, MartinCarrera)
        L7 = SubwayLine("Línea 7", "L7", ElRosario, BarrancaDelMuerto)
        L8 = SubwayLine("Línea 8", "L8", Garibaldi, ConstitucionDe1917)
        L9 = SubwayLine("Línea 9", "L9", Tacubaya, Pantitlan)
        L12 = SubwayLine("Línea 12", "L12", Mixcoac, Tlahuac)
        LA = SubwayLine("Línea A", "LA", Pantitlan, LaPaz)
        LB = SubwayLine("Línea B", "LB", Buenavista, CiudadAzteca)

        self.set_subway_lines([L1, L2, L3, L4, L5, L6, L7, L8, L9, L12, LA, LB])

        print("\n---> Controlador Inicializado <---")