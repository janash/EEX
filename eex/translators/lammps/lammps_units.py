# Units based LAMMPS unit styles (http://lammps.sandia.gov/doc/units.html)

_units_style = {
    "lj": {},
    "real": {
        "[mass]": "(gram mol ** -1)",
        "[length]": "angstrom",
        "[time]": "femtosecond",
        "[energy]": "(kcal mol ** -1)",
        "[velocity]": "(angstrom femtosecond ** -1)",
        "[force]": "(kcal * mol ** -1 angstrom ** -1)",
        "[torque]": "(kcal * mol ** -1)",
        "[temperature]": "kelvin",
        "[pressure]": "atmosphere",
        "[dynamic viscosity]": "poise",
        "[charge]": "e",
        "[dipole]": "e * angstrom",
        "[electric field]": "(volt angstrom ** -1)",
        "[density]": "(gram cm ** -dim"
    },
    "metal": {
        "[mass]": "(gram mol ** -1)",
        "[length]": "(angstrom)",
        "[time]": "(picosecond)",
        "[energy]": "(eV)",
        "[velocity]": "(angstrom picosecond ** -1)",
        "[force]": "(eV angstrom ** -1)",
        "[torque]": "(eV)",
        "[temperature]": "(kelvin)",
        "[pressure]": "(bar)",
        "[dynamic viscosity]": "(poise)",
        "[charge]": "(e)",
        "[dipole]": "(e * angstrom)",
        "[electric field]": "(volt angstrom ** -1)",
        "[density]": "(gram cm ** -dim)",
    },
    "si": {
        "[mass]": "(kilogram)",
        "[length]": "(meter)",
        "[time]": "(second)",
        "[energy]": "(joule)",
        "[velocity]": "(meter second ** -1)",
        "[force]": "(newtons)",
        "[torque]": "(newton meter)",
        "[temperature]": "(kelvin)",
        "[pressure]": "(pascal)",
        "[dynamic viscosity]": "(pascal second)",
        "[charge]": "(coulomb)",
        "[dipole]": "(coulomb meter)",
        "[electric field]": "(volt meter ** -1)",
        "[density]": "(kilogram meter ** -dim)",
    },
    "cgs": {
        "[mass]": "(gram)",
        "[length]": "(centimeters)",
        "[time]": "(second)",
        "[energy]": "(ergs)",
        "[velocity]": "(centimeters second ** -1)",
        "[force]": "(dyne)",
        "[torque]": "(dyne cen[time]ters)",
        "[temperature]": "(kelvin)",
        "[pressure]": "(dyne cm ** -2)",
        "[dynamic viscosity]": "(poise)",
        "[charge]": "(statcoulombs)",
        "[dipole]": "(statcoulombs cen[time]ter)",
        "[electric field]": "(statvolt cm ** -1)",
        "[density]": "(gram cm ** -dim)",
    },
    "electron": {
        "[mass]": "(amu)",
        "[length]": "(Bohr)",
        "[time]": "(femtosecond)",
        "[energy]": "(hartree)",
        "[velocity]": "(Bohr (atomic [time] unit) ** -1)",
        "[force]": "(hartree Bohr ** -1)",
        "[temperature]": "(kelvin)",
        "[pressure]": "(pascal)",
        "[charge]": "(e)",
        "[dipole] moment": "(debye)",
        "[electric field]": "(volt cm ** -1)",
    },
    "micro": {
        "[mass]": "(picogram)",
        "[length]": "(micrometer)",
        "[time]": "(microsecond)",
        "[energy]": "(picogram micrometer ** 2 microsecond ** -2)",
        "[velocity]": "(micrometers microsecond ** -1)",
        "[force]": "(picogram micrometer microsecond ** -2)",
        "[torque]": "(picogram micrometer ** 2 microsecond ** -2)",
        "[temperature]": "(kelvin)",
        "[pressure]": "(picogram micrometer ** -1 microsecond ** -2)",
        "[dynamic viscosity]": "(picogram micrometer ** -1 microsecond ** -1)",
        "[charge]": "(picocoulomb)",
        "[dipole]": "(picocoulomb micrometer)",
        "[electric field]": "(volt micrometer ** -1)",
        "[density]": "(picogram micrometer ** -dim"
    },
    "nano": {
        "[mass]": "(attogram)",
        "[length]": "(nanometer)",
        "[time]": "(nanosecond)",
        "[energy]": "(attogram nanometer ** 2 nanosecond ** -2)",
        "[velocity]": "(nanometers nanosecond ** -1)",
        "[force]": "(attogram nanometer nanosecond ** -2)",
        "[torque]": "(attogram nanometer ** 2 nanosecond ** -2)",
        "[temperature]": "(kelvin)",
        "[pressure]": "(attogram nanometer ** -1 nanosecond ** -2)",
        "[dynamic viscosity]": "(attogram nanometer ** -1 nanosecond ** -1)",
        "[charge]": "(e)",
        "[dipole]": "(e nanometer)",
        "[electric field]": "(volt nanometer ** -1)",
    },
}

if __name__ == "__main__":
    from eex.units import ureg
    for k, v in _units_style.items():
        for k, v in _units_style[k].items():
            try:
                u = ureg.parse_expression(v)
                # print(u)
            except:
                print("Pint could not parse %s" % v)
