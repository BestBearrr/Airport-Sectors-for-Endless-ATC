# Singapore TMA v3.0

**Version 3.0** *by BestBearrr*

**This readme is for version 3.0 and above, featuring the airspace and procedures in use from 21 March 2024. For the old airspace and procedures, use version 2.2 (2023). **

An attempt at recreating the Singapore TMA, with the following airports:

1. WSSS – Singapore Changi Airport
2. WSSL – Singapore Seletar Airport
3. WIDD – Batam Hang Nadim Airport
4. WMKJ – Johor Senai Airport

### Features

------

* Compatible with v2.2 (2023)
  * v3.0 is labelled WSSS, v2.2 (2023) is labelled WSSX
* Realignment of Singapore-Jakarta FIR
* New airspace and procedures effective 21 March 2024
* SIDs and STARs, or flight planned routes, for each airport
* Accurate airlines and plane types operating at each airport in 2024 or later as much as possible
* Revised climb/descent rates for each aircraft type for more realism
* Minimum separation indicator between aircraft on final approach
* Updates to coastlines

### Installation

------

For PC,

1. Place WSSS.txt in the folder `Endless ATC/locations`

For Android,

1. Place WSSS.txt in the folder `android/data/com.dirgtrats.endlessatc/files/` 

   *(You may need to connect your phone via USB to your computer, or use a file explorer app that allows access to the data folder)*

### Overview

------

Heads-up: Controlling in the Singapore TMA can be challenging! The cluster of airports and narrow airspace available pose a challenge. If the weather is bad such that (particularly during the monsoon season) aircraft require to deviate, it becomes even more difficult.

Are you ready to vector planes? While there are SIDs and STARs, due to the nature of the airspace and procedures, radar vectoring will be essential here. Not only must aircraft be vectored to final, but also for sequencing, track shortening, maintaining separation between planes bound for different airports, or weather deviation.

Hope you have as much fun as I did creating this!

------

Transition Altitude: 11000ft
Transition Level: FL130
Any level in between, like FL120, should not be assigned to aircraft.

In Endless ATC, STARs are implemented as 'approach routes'. To clear an aircraft on a STAR, it needs to be flying towards an applicable fix, then you can activate the APP button for the STAR.

The table below shows the skill points at which an airport or runway is unlocked.

| Skill Level | Airport unlocked |                      Runway(s) unlocked                      |
| :---------: | :--------------: | :----------------------------------------------------------: |
|    START    |       WSSS       | Runway 1 (02L/20R) for arrivals<br />Runway 2 (02C/20C) for arrivals & departures |
|     10      |       WSSL       |                         Runway 03/21                         |
|     15      |       WIDD       |                         Runway 04/22                         |
|     22      |       WMKJ       |                          Runway 16                           |
|     35      |        -         |      WSSS Runway 1 (02L/20R) for arrivals & departures       |

The table below shows the various runway configurations available for use.

* Note that <u>odd-numbered configurations are North flow (runway 02)</u> while <u>even-numbered configurations are South flow (runway 20)</u>.

|        Runway Configuration        |                      Airports Available                      |
| :--------------------------------: | :----------------------------------------------------------: |
|                1, 2                |                           **All**                            |
|                3, 4                |                       WSSS, WSSL, WIDD                       |
|                5, 6                |                          WSSS, WSSL                          |
|                7, 8                |                          WSSS, WIDD                          |
| 9, 10<br />*(Oct 2020 - Nov 2023)* | **All<br />**Note: WSSS Rwy 2 (02C/20C) closed, while Rwy 1 (02L/20R) and Rwy 3 (02R/20L) in use. |
|       11, 12<br/>*(Future)*        |                      WSSS Three Runways                      |

If using **<u>custom traffic flow rate</u>**, a realistic rate (each for arrivals and departures) would be:

* Up to 30-35/h for a chill and relaxing experience
* 35-45/h to experience a typical peak period
* Over 45/h for a very busy and intense experience

For WSSS, the movement rate of one runway is about 34/h at peak due to a mix of narrow and widebody aircraft using the runway.

- **Note: SIDs and STARs with a '>' prefix indicate radar vectoring required. This is applicable to certain airports or procedures.**



### WSSS – Singapore Changi Airport

------

#### Runway information

Runway 1 (02L/20R): Primary Landing Runway

Runway 2 (02C/20C): Primary Departure Runway

Runway 3 (02R/20L): Not available for civil use until further advised

Segregated Mode of Operations: Rwy 1 is the primary landing runway while Rwy 2 is the primary departure runway.

![WSSS Overview](WSSS overview v3.png)

#### Departure Procedures

* **Initial climb: 3000ft**

* Take note of minimum altitude restrictions, in particular to the north/west.

  * Planes must also not infringe WIDD (Batam) Control Zone. Planes must be at or above 4000ft.

* Departures can be cleared for high speed climb at your discretion.

* If there is a **simultaneous departure on Runway 1 (02L/20R)**, then the departure on Runway 2 (02C/20C) may be turned to a diverging heading of 040°/180° to ensure initial separation.

* **Departures from Runway 3 (02R/20L)**

  Runway 02R departures will climb on runway heading 023° and require initial vectors to either `AKOMA` or `HOSBA`, which is the first waypoint of the SID (C-suffix).

  Runway 20L departures will follow the respective SID (D-suffix).

  Note: This runway is currently not available for civil use, but nevertheless it is available for use in runway configurations 9 and 10 should you desire.

* `VOVOS` SIDs are not in use until further advised, thus they are deactivated in this file.


|  Runway   | SID Suffix |
| :-------: | :--------: |
| 02L / 20R |   E / F    |
| 02C / 20C |   A / B    |
| 02R / 20L |   C / D    |

#### Arrival Procedures

**STAR Suffix: Runway 02 - 'A', Runway 20 - 'B'**

STARs are designed to be only runway direction specific (and not for a specific runway), with a vector to final from the last waypoint of the STAR (which is located near the final approach area) to final approach. However, at any time if required, you may opt to radar vector planes.

- Last waypoint of the STARs:
  - Rwy 02: `SANAT`, `SAMKO`
  - Rwy 20: `NYLON`, `BIPOP`, `BIDUS`

* Note: Arrivals to WSSS from
  * `Y514 NUFFA` shall route direct to ` PIBAP` to join the MABAL STAR. (routing: `NUFFA direct PIBAP`)
  * `A464 ARAMA` shall route direct to `TEBUN` to join the TEBUN STAR. (routing: `ARAMA direct TEBUN`)
* Speeds like 280 knots may be assigned to aircraft for sequencing.

Arrivals converge at four waypoints (known as "entry gates"). Holdings are typically carried out at, but not limited to, these waypoints.

* North: `PASPU`
* East: `KEXAS`
* South: `REMES`
* West: `VAMPO`

- STARs may contain an altitude point to better simulate the *(actual)* descent profile of a plane as it enters the approach airspace.
- When WSSS runway 20 is in use,
  - For arrivals via `A464 ARAMA`, the default STAR will be `TEBUN1B`. The alternative shorter STAR, `LELIB3B`, may be offered by ATC when traffic permits, aka whenever you wish to.
    - When the plane is headed towards waypoint `ARAMA`, click on the APP button **<u>once</u>** for `TEBUN1B` or **<u>twice</u>** for `LELIB3B`.
  - A small thing to note: Rwy 20R has a displaced threshold of 740m southwards, so the final approach profile for Rwy 20R is in fact similar to that of Rwy 20C and 20L. (i.e. if referring to the runway extended centerline in the game, the depicted profile is slightly different from reality due to the displaced threshold)



More information on the approach procedures:

- **Speed control:** **180 knots by 8 NM** from touchdown, thereafter **150 knots until 4 NM** from touchdown.
- Handoff to Tower anywhere within ~10nm.

* **ILS Approach to runway 02L / 20R**

  * Usually, planes are cleared to intercept the localizer first, and only when established on the localizer that they are cleared for the ILS approach (localizer + glideslope).
* Most of the time, planes are cleared to descend to **2500ft** to intercept, but other altitudes are alright too.
  
* **RNP Approach to runway 20L**

  * Vector aircraft as usual, when nearing the extended centerline or as appropriate, direct the aircraft to `OBGIS`* and clear the aircraft for the RNP approach. Descend the aircraft to 2000ft then/or to **1700ft**.

    _* `OBGIS` is the intermediate fix of the approach._

* **Simultaneous (independent/dependent) parallel approaches to both runways**

  * Used especially during periods of high arrival traffic/congestion. Increases landing capacity as both runways are utilised for landings. Ensure planes are separated by at least 3nm or 1000ft until localizer intercept.
  
* **Missed Approach/Go Around**

  * Continue on runway heading and climb to 3000ft or as appropriate (e.g. 4000ft).

* **Wake Turbulence Separation** 

  * ICAO RECAT separation is applied between landing aircraft.
  * Along the extended centreline on final approach, an indicator line shows the minimum required separation between the preceding and succeding aircraft.

#### Further notes:

- **Potential conflict areas between climbing departures and descending arrivals:**

* **<u>Runway 02 direction:</u>**
  * Near `VANBU` & `VIMAL` waypoints
    * **Climb departures to no higher than 9000ft (`VANBU`)** and **descend arrivals to no lower than 10000ft (`VIMAL`)**.
* **<u>Runway 20 direction:</u>**
  * Near `ERVIV` & `BITAM` waypoints
    * **Climb departures to no higher than 6000ft (`ERVIV`)** and **descend arrivals to no lower than 7000ft (`BITAM`)**.
  * Near `SEBVO` & `LAVAX` waypoints
    * **Climb departures to no higher than 9000ft (`SEBVO`)** and **descend arrivals to no lower than 10000ft (`LAVAX`)**.



### WSSL – Singapore Seletar Airport

------

#### Runway information

Runway 03/21: Visual approach only

Rwy 03 glidepath: 3.2°
Rwy 21 glidepath: 3.5°

Seletar is a challenging airport to land at or depart from. With a really tight control zone, nearby runways with similar orientation, and noise abatement areas, pilots have to be careful to keep all turns within the Seletar Control Zone while landing at the correct airport and complying with noise abatement procedures.

* For Seletar, there is no SID or STAR. Instead, **departure and joining procedures (arrival) from the North and the South** form the backbone of WSSL's routing.
  * **Via the North:** Waypoint `OMKOM`
  * **Via the South:** The procedure `SJ-PONJO-RECHI` (for arrivals) or its inverse `RECHI-PONJO-SJ` (for departures)

#### Departure Procedures

* **Initial climb: 3000ft**
* Runway 03 departures (to the North) are assigned heading 360
* Runway 21 departures (to the South) track `RECHI-PONJO-SJ` before being vectored to their final waypoint.
  * Vector departures to their exit waypoints. Ensure separation with other traffic and altitude restrictions.
  * Deviation is not permitted on `RECHI-PONJO` or `RECHI-PONJO-SJ`.



* *The following are not implemented in this file, but you may vector planes as such if you wish to simulate it.*
  * *Rwy 03 departures may turn left for downwind to track `SETHI-RECHI-PONJO-SJ` to depart to the South.*
  * *Rwy 21 departures may turn right for downwind, then fly heading 360 to depart to the North.*
  * *Reminder that aircraft are to keep all turns within Seletar Control Zone.*

#### Arrival Procedures

By default, arrivals continue on their flight planned routes towards WSSL with the final waypoint being `OMKOM` or  `SJ`. This may or may not be the ideal routing in the airspace. As such, **radar vectors <u>will be necessary</u> to bring arrivals towards the airport**.

During congestion or bad weather, there may be a need to delay aircraft. Tactically issue holding instructions or delay vectors to aircraft.

* For approaches via the North, planes will be vectored to position for visual approach to the runway.

* For approaches via the South, planes will be instructed to proceed direct to `SJ` (or `PONJO` if available), to track via `SJ-PONJO-RECHI` for visual approach to the runway. Aircraft are to strictly follow `SJ-PONJO-RECHI` or `PONJO-RECHI` routing; deviation is not permitted.



**The joining procedures are outlined in greater detail below.** 

![WSSL rwy 03 approach](WSSL rwy 03.png)

* <u>**Runway 03:**</u>
  * From the North: Position to join <u>left-hand downwind</u> to runway 03 via either of the two 'helper points', `VIS03A` or `VIS03B`, **at 1500ft**.
  * From the South: Track direct to `SJ` or `PONJO` , following the `SJ-PONJO-RECHI` joining procedure for a <u>**straight-in visual approach**</u> to runway 03.

![WSSL rwy 21 approach](WSSL rwy 21.png)

* <u>**Runway 21:**</u>
  * From the North: Position to join final for a <u>**straight-in visual approach**</u> to runway 21 via the 'helper point', `VIS21`, **at 2000ft** (or 1500ft).
  * From the South: Track direct to `SJ` or `PONJO`, following the `SJ-PONJO-RECHI-SETHI` joining procedure for a <u>right-hand downwind</u> to runway 21.
* In particular for approaches via downwind,
  * Aircraft are to keep all turns within Seletar Control Zone.
  * *Also note that in the game, some aircraft may not be able to make the turn from downwind to final to land due to higher speeds. They will make a go around and you can bring them around to join for a straight-in approach instead of via downwind.*

**Tip:** You can temporarily use a different runway config to allow a plane to land on the opposite side of your active flow. This may be particularly useful for WSSL.

Take note maximum tailwind component of 10 knots is allowed for landings. Also if planes are unable to land due to weather, then they should be in holdings or diverted.



### WIDD – Batam Hang Nadim Airport

------

#### Runway information

Runway 04: ILS approach

Runway 22: Only RNP approach

*In real life, the initial departure and final approach segments (at or below 3000ft) are controlled by Tanjung Pinang Approach Control, but it is not possible to make this distinction in game.*

#### Departure Procedures

* **Initial climb: 3000ft**
* Departures to the North (to `SABKA A457` / `AROSO Y513` / `VMR`) will climb on runway heading and require radar vectors to their final waypoint. Aircraft may pass through Changi Control Zone at or above 4000ft.
* Departures to all other waypoints will follow their respective SIDs. (Example: To waypoint `MIBEL` via `MIBEL1J` or `MIBEL1M` SID)
* Ensure separation with other traffic and altitude restrictions.

| Runway  | SID Suffix |
| :-----: | :--------: |
| 04 / 22 |   J / M    |

#### Arrival Procedures

**STAR Suffix: P**

* Note: Arrivals to WIDD from
  * `A464 ARAMA` shall route direct to `GUNAN` to join the GUNAN STAR. (routing: `ARAMA direct GUNAN`)
  * (North) `VMR` will initially continue on their flight planned route towards `BTM` (about the same position as `BITAM`) and will require radar vectors towards the airport.
  * all other waypoints will follow the respective STAR to `TUSPI`.
* STAR will end at `TUSPI` thereafter clear aircraft for ILS approach to runway 04 or RNP approach to runway 22.
* If traffic permits, track shortening may be offered to the final approach course.

* Runway 04: Descend to 2000ft for ILS approach.
* Runway 22: Descend to 2000ft for RNP approach. Use the 'helper point' `RNP22`.
* *Visual approaches may be conducted in real life, but are not implemented.*



### WMKJ – Johor Senai Airport

------

#### Runway information

Runway 16: ILS approach
*Runway 34 is not implemented as it is rarely used for arrivals; only visual approach (or RNP Z (AR) for authorised aircraft) available.*

*In real life, the initial departure and approach segments in the Johor TMA are controlled by Johor Radar, but it is not possible to make this distinction in game.*

Singapore provides air traffic control services only for departures and arrivals to the North (via `VMR`), East (via `G580`) and South (via `G579`, `B470`), thus only these are implemented.

In game, planes will mainly route via `ADLOV` SID/STAR, `OMKOM` SID/STAR or `PIMOK` STAR for arrivals.

#### Departure Procedures

* **Initial climb: 6000ft**
* Departures are cleared via `OMKOM1E` departure to `OMKOM`, then onto their flight planned routes. There may or may not be a need to vector aircraft.
* To keep clear of prohibited area WMP228.

| Runway | SID Suffix |
| :----: | :--------: |
|   16   |     E      |

#### Arrival Procedures

**STAR Suffix: J**

By default, arrivals continue on their flight planned routes then on the STAR towards WMKJ (`ADLOV2J/PIMOK2J/OMKOM2J`). This may or may not be the ideal routing in the airspace. As such, **radar vectors <u>may be needed</u> to bring arrivals towards the airport**.

* Runway 16: **Descend to 6000ft** at `PIMOK`/`OMKOM` to join `PIMOK2J`/`OMKOM2J` arrival, which will guide the aircraft to descend to 2000ft for ILS approach.
* *RNP Z (AR) approach for authorised aircraft may be conducted but is not implemented here.*



### Known Issues/Limitations

------

1. Conflicts between inbound planes may arise around the entry points near the airspace boundary if the game generates the planes too close to one another. Unfortunately this is RNG.
2. WSSL: The game may generate a departure from runway 03 while another plane is positioning for left hand downwind visual approach to runway 03 from the north (via `VIS03A`/`VIS03B` 'helper points'). This may cause a conflict, so be careful and hope a departure isn't generated.
3. WSAP Paya Lebar Airport and WIDN Tanjung Pinang Airport are deliberately not included owing to the low traffic volume at these airports.
4. Some coastlines could be better depicted. May improve at a later date. (It takes a lot of effort...)

### Changelog

------

**Version 3.0** released on 23 February 2025. Developed by BestBearrr.

* Compatibility with version 2.2 (2023)

- Realignment of Singapore-Jakarta FIR
- New and updated SID/STAR and approach procedures
- Revised climb and descent rates of aircraft for more realism
- Added rarely used LEBAR STAR transition for WSSS
- Added ADLOV SID/STAR for WMKJ departures and arrivals to/from the North
- Updated airlines/planes operating in 2024 or later
  - Added Scoot's Embraer E190-E2 jet, Qantas' Airbus A220 Darwin-Singapore flights
  - Replaced Batik Air Malaysia's ATR 72-500 flights to Batam with Boeing 737 MAX 8 
  - Removed airlines that have ceased flights to any of the airports
  - Other minor changes
- Updates to coastlines
- Colours
- Various adjustments/bug fixes

**Version 2.2 (2023)** released on 23 February 2025. Developed by BestBearrr.

- Compatibility with version 3.0
- Revised climb and descent rates of aircraft for more realism
- Added ADLOV SID/STAR (north) for WMKJ
- Updates to coastlines
- Colours
- Various adjustments/bug fixes

**Version 2.1 (2023)** released on 16 January 2024. Developed by BestBearrr.

- Added WIDD, WMKJ airports
- Added WSSS Runway 02C/20C, Improved WSSL
- Updated controllable airspace boundary in game
- Added various runway configurations for more options
- Adjustments to prohibited/restricted/danger areas
- Minor enhancements to procedures
- Modifications to the characteristics of some plane types, mainly to allow the speed assignment of 150 knots

**Version 2.0** released on 31 December 2022. Developed by BestBearrr.

- Initial release of Singapore TMA with WSSS and WSSL
  - WSSS interim runway 02R/20L

**Version 1.3** released on 11 August 2021. Developed by Jacob.

_Disclaimer: The information included herein is not meant to be realistic, but for recreational use only._
