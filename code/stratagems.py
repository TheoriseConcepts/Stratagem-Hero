from typing import List

class Stratagem:
    def __init__  (self, name: str, inputs: List[str], icon: str, category: str):
        self.name = name
        self.inputs = inputs
        self.icon = icon
        self.category = category

Stratagems = {
    'Patriotic Administration Center': [
        Stratagem('Machine Gun', ['down', 'left', 'down', 'up', 'right'], 'Machine Gun.svg', 'Supply'),
        Stratagem('Anti-Materiel Rifle', ['down', 'left', 'right', 'up', 'down'], 'Anti-Material Rifle.svg', 'Supply'),
        Stratagem('Stalwart', ['down', 'left', 'down', 'up', 'up', 'left'], 'Stalwart.svg', 'Supply'),
        Stratagem('Expendable Anti-Tank', ['down', 'down', 'left', 'up', 'right'], 'Expendable Anti-Tank.svg', 'Supply'),
        Stratagem('Recoilless Rifle', ['down', 'left', 'right', 'right', 'left'], 'Recoilless Rifle.svg', 'Supply'),
        Stratagem('Flamethrower', ['down', 'left', 'up', 'down', 'up'], 'Flamethrower.svg', 'Supply'),
        Stratagem('Autocannon', ['down', 'left', 'down', 'up', 'up', 'right'], 'Autocannon.svg', 'Supply'),
        Stratagem('Railgun', ['down', 'right', 'down', 'up', 'left', 'right'], 'Railgun.svg', 'Supply'),
        Stratagem('Spear', ['down', 'down', 'up', 'down', 'down'], 'Spear.svg', 'Supply'),
    ],
    'Orbital Cannons': [
        Stratagem('Orbital Gatling Barrage', ['right', 'down', 'left', 'up', 'up'], 'Orbital Gatling Barrage.svg', 'Offensive'),
        Stratagem('Orbital Airburst Strike', ['right', 'right', 'right'], 'Orbital Airburst Strike.svg', 'Offensive'),
        Stratagem('Orbital 120MM HE Barrage', ['right', 'right', 'down', 'left', 'right', 'down'], 'Orbital 120MM HE Barrage.svg', 'Offensive'),
        Stratagem('Orbital 380MM HE Barrage', ['right', 'down', 'up', 'up', 'left', 'down', 'down'], 'Orbital 380MM HE Barrage.svg', 'Offensive'),
        Stratagem('Orbital Walking Barrage', ['right', 'down', 'right', 'down', 'right', 'down'], 'Orbital Walking Barrage.svg', 'Offensive'),
        Stratagem('Orbital Laser', ['right', 'down', 'up', 'right', 'down'], 'Orbital Laser.svg', 'Offensive'),
        Stratagem('Orbital Railcannon Strike', ['right', 'up', 'down', 'down', 'right'], 'Orbital Railcannon Strike.svg', 'Offensive'),
    ],
    'Hangar': [
        Stratagem('Eagle Strafing Run', ['up', 'right', 'right'], 'Eagle Strafing Run.svg', 'Offensive'),
        Stratagem('Eagle Airstrike', ['up', 'right', 'down', 'right'], 'Eagle Airstrike.svg', 'Offensive'),
        Stratagem('Eagle Cluster Bomb', ['up', 'right', 'down', 'down', 'right'], 'Eagle Cluster Bomb.svg', 'Offensive'),
        Stratagem('Eagle Napalm Airstrike', ['up', 'right', 'down', 'up'], 'Eagle Napalm Airstrike.svg', 'Offensive'),
        Stratagem('Jump Pack', ['down', 'up', 'up', 'down', 'up'], 'Jump Pack.svg', 'Supply'),
        Stratagem('Eagle Smoke Strike', ['up', 'right', 'up', 'down'], 'Eagle Smoke Strike.svg', 'Offensive'),
        Stratagem('Eagle 110MM Rocket Pods', ['up', 'right', 'up', 'left'], 'Eagle 110MM Rocket Pods.svg', 'Offensive'),
        Stratagem('Eagle 500KG Bomb', ['up', 'right', 'down', 'down', 'down'], 'Eagle 500KG Bomb.svg', 'Offensive'),
        Stratagem('Eagle Rearm', ['up', 'up', 'left', 'up', 'right'], 'Eagle Rearm.svg', 'Offensive'),
    ],
    'Bridge': [
        Stratagem('Orbital Precision Strike', ['right', 'right', 'up'], 'Orbital Precision Strike.svg', 'Offensive'),
        Stratagem('Orbital Gas Strike', ['right', 'right', 'down', 'right'], 'Orbital Gas Strike.svg', 'Offensive'),
        Stratagem('Orbital EMS Strike', ['right', 'right', 'left', 'down'], 'Orbital EMS Strike.svg', 'Offensive'),
        Stratagem('Orbital Smoke Strike', ['right', 'right', 'down', 'up'], 'Orbital Smoke Strike.svg', 'Offensive'),
        Stratagem('HMG Emplacement', ['down', 'up', 'left', 'right', 'right', 'left'], 'HMG Emplacement.svg', 'Defensive'),
        Stratagem('Shield Generator Relay', ['down', 'down', 'left', 'right', 'left', 'right'], 'Shield Generator Relay.svg', 'Defensive'),
        Stratagem('Tesla Tower', ['down', 'up', 'right', 'up', 'left', 'right'], 'Tesla Tower.svg', 'Defensive'),
    ],
    'Engineering Bay': [
        Stratagem('Anti-Personnel Minefield', ['down', 'left', 'up', 'right'], 'Anti-Personnel Minefield.svg', 'Defensive'),
        Stratagem('Supply Pack', ['down', 'left', 'down', 'up', 'up', 'down'], 'Supply Pack.svg', 'Supply'),
        Stratagem('Grenade Launcher', ['down', 'left', 'up', 'left', 'down'], 'Grenade Launcher.svg', 'Supply'),
        Stratagem('Laser Cannon', ['down', 'left', 'down', 'up', 'left'], 'Laser Cannon.svg', 'Supply'),
        Stratagem('Incendiary Mines', ['down', 'left', 'left', 'down'], 'Incendiary Mines.svg', 'Defensive'),
        Stratagem('"Guard Dog" Rover', ['down', 'up', 'left', 'up', 'right', 'right'], 'Guard Dog Rover.svg', 'Supply'),
        Stratagem('Ballistic Shield Backpack', ['down', 'left', 'down', 'down', 'up', 'left'], 'Ballistic Shield Backpack.svg', 'Supply'),
        Stratagem('Arc Thrower', ['down', 'right', 'down', 'up', 'left', 'left'], 'Arc Thrower.svg', 'Supply'),
        Stratagem('Quasar Cannon', ['down', 'down', 'up', 'left', 'right'], 'Quasar Cannon.svg', 'Supply'),
        Stratagem('Shield Generator Pack', ['down', 'up', 'left', 'right', 'left', 'right'], 'Shield Generator Pack.svg', 'Supply'),
    ],
    'Robotic Workshop': [
        Stratagem('Machine Gun Sentry', ['down', 'up', 'right', 'right', 'up'], 'Machine Gun Sentry.svg', 'Defensive'),
        Stratagem('Gatling Sentry', ['down', 'up', 'right', 'left'], 'Gatling Sentry.svg', 'Defensive'),
        Stratagem('Mortar Sentry', ['down', 'up', 'right', 'right', 'down'], 'Mortar Sentry.svg', 'Defensive'),
        Stratagem('Guard Dog', ['down', 'up', 'left', 'up', 'right', 'down'], 'Guard Dog.svg', 'Supply'),
        Stratagem('Autocannon Sentry', ['down', 'up', 'right', 'up', 'left', 'up'], 'Autocannon Sentry.svg', 'Defensive'),
        Stratagem('Rocket Sentry', ['down', 'up', 'right', 'right', 'left'], 'Rocket Sentry.svg', 'Defensive'),
        Stratagem('EMS Mortar Sentry', ['down', 'up', 'right', 'down', 'right'], 'EMS Mortar Sentry.svg', 'Defensive'),
        Stratagem('Patriot Exosuit', ['left', 'down', 'right', 'up', 'left', 'down', 'down'], 'Patriot Exosuit.svg', 'Defensive'),
    ],
    'Mission Stratagems': [
        Stratagem('Resupply', ['down', 'down', 'up', 'right'], 'Resupply.svg', 'Mission'),
        Stratagem('Reinforce', ['up', 'down', 'right', 'left', 'up'], 'Reinforce.svg', 'Mission'),
        Stratagem('SOS Beacon', ['up', 'down', 'right', 'up'], 'SOS Beacon.svg', 'Mission'),
        Stratagem('Upload Data', ['down', 'down', 'up', 'up', 'up'], 'Upload Data.svg', 'Mission'),
        Stratagem('Hellbomb', ['down', 'up', 'left', 'down', 'up', 'right', 'down', 'up'], 'Hellbomb.svg', 'Mission'),
        Stratagem('SEAF Artillery', ['right', 'up', 'up', 'down'], 'SEAF Artillery.svg', 'Mission'),
        Stratagem('Seismic Probe', ['up', 'up', 'left', 'right', 'down', 'down'], 'Seismic Probe.svg', 'Mission'),
        Stratagem('Prospecting Drill', ['down', 'down', 'left', 'right', 'down', 'down'], 'Prospecting Drill.svg', 'Mission'),
        Stratagem('Orbital Illumination Flare', ['right', 'right', 'left', 'left'], 'Orbital Illumination Flare.svg', 'Mission'),
        Stratagem('Super Earth Flag', ['down', 'up', 'down', 'up'], 'Super Earth Flag.svg', 'Mission'),
    ],
}
