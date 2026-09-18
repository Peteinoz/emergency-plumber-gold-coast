from _common import *

page = dict(
    slug="pumps", kind="service", crumb="Pumps",
    title="Pump Repairs & Installation Gold Coast | Moyle Plumbing",
    description='Pump repairs and installation for rainwater tanks, pressure systems, sumps and sewage pumps on the Gold Coast and Logan. Call (07) 3807 7327.',
    h1="Pump repairs and installation",
    eyebrow="Pumps and tanks",
    intro="<p>Pump repairs and installation cover a lot of ground: the pressure pump on a rainwater tank, the submersible in a basement sump, the macerator behind a downstairs toilet and the sewage pump station on an acreage block. Moyle Plumbing &amp; Gasfitting repairs, replaces and installs all of them across the northern Gold Coast, Logan and out to the Redlands.</p>",
    breadcrumb=[("all-services-available", "Services")],
    service=dict(name="Pump repair and installation", area="Gold Coast"),
    body=sec("""
<h2>Pump types we work on</h2>
""" + cards([
    ("plumber-mount-cotton", "Rainwater tank pressure pumps", "The pump that gives an acreage home its water pressure. Constant-pressure, multi-stage and pumps with automatic mains changeover."),
    ("blocked-drains", "Sewage and effluent pumps", "Pump stations for homes below the sewer, septic and treatment plant transfer pumps, and grinder pumps."),
    ("leak-repairs", "Sump and stormwater pumps", "Submersibles that keep basements, lift pits and low driveways from flooding in a Gold Coast downpour."),
    ("toilets", "Macerators", "Compact pumps that let a toilet or laundry be added where gravity drainage is not possible."),
    ("hot-water", "Hot water circulating pumps", "Ring-main pumps that deliver instant hot water to far taps in larger homes."),
    ("plumber-redland-bay", "Bore and transfer pumps", "Moving water from a bore, dam or tank to where it is used."),
]) + """
""") + soft("""
<h2>Symptoms and what they usually mean</h2>
<table>
<thead><tr><th>Symptom</th><th>Likely cause</th></tr></thead>
<tbody>
<tr><td>Pump runs but no pressure</td><td>Empty tank, blocked foot valve or strainer, lost prime, worn impeller</td></tr>
<tr><td>Pump cycles on and off constantly</td><td>Leak on the pressure side, failed pressure tank, faulty controller</td></tr>
<tr><td>Pump will not start</td><td>Power supply, tripped thermal overload, seized motor, failed controller</td></tr>
<tr><td>Pump runs continuously</td><td>Large leak, pressure switch set wrong, pump too small for the demand</td></tr>
<tr><td>Sewage pump alarm</td><td>Float switch fouled, pump blocked with wipes, failed pump</td></tr>
<tr><td>Pump noisy or vibrating</td><td>Cavitation from restricted suction, bearing failure, loose mount</td></tr>
</tbody>
</table>
<p>A pump that runs on and off overnight with no taps open is usually telling you about a leak, not a pump fault. We check for that first. See """ + L("leak-repairs", "leak detection") + """.</p>
""") + sec("""
<h2>Repair or replace</h2>
<p>Pressure switches, controllers, capacitors, foot valves and pressure tanks are all replaceable, and often the cheaper answer. A pump with a seized motor, a cracked casing or one that has simply been undersized from the start is better replaced with a unit matched to the household. We size a replacement on the number of outlets, the height of the house and the tank arrangement, not just on what was there before.</p>
<h2>Installation and mains changeover</h2>
<p>For homes with both tank and town water we fit automatic changeover valves so the house switches to mains when the tank runs low, without anyone noticing. Tank-only properties get a pump with dry-run protection so an empty tank does not burn the motor out. On sewage pump stations we install high-level alarms and, where it matters, dual pumps so one failure does not close the bathroom.</p>
<p>Pumps fill many of our days on the acreage around """ + L("plumber-mount-cotton", "Mount Cotton") + """, """ + L("plumbing-services-alberton", "Alberton") + """ and """ + L("plumber-redland-bay", "Redland Bay") + """. A dead pump on a tank-only property means no water at all, so it goes on the urgent list with everything on the """ + H("emergency callout page") + """. Company details and history: """ + M("the Moyle Plumbing website") + """.</p>
""") + sec("""
<h2>Pressure tanks and controllers</h2>
<p>Two parts decide how a pressure pump behaves. A pressure tank, where fitted, stores a small volume under pressure so the pump does not start every time a tap is cracked open; when its internal bladder fails, the pump short-cycles and wears out fast. An electronic controller starts the pump on demand and stops it on loss of flow, with dry-run protection built in; when it fails, the symptoms look like a dead pump. Both are far cheaper than a new pump, and both are checked before we recommend replacing anything. For homes where the pump is close to bedrooms, a controller with a soft start and a tank to reduce cycling makes a noticeable difference at night.</p>
"""),
    faqs=[
        ("My pump runs every few minutes at night. Is it broken?",
         "<p>Probably not. It is holding pressure against a leak somewhere, often a toilet cistern, a dripping tap or a split irrigation line. Isolate sections until the cycling stops and you have found the culprit, or ask us to trace it.</p>"),
        ("How long does a tank pump last?",
         "<p>A well-sized pump with clean water and dry-run protection can run for many years. Pumps that cycle constantly against a leak, run dry or sit in full sun and weather wear out much faster.</p>"),
        ("Can you add a pump to an existing rainwater tank?",
         "<p>Yes. We fit the pump, the pressure controller, a filter and the pipework to the house, and a changeover to mains if the property has town water.</p>"),
        ("What should not go into a sewage pump station?",
         "<p>Wipes, sanitary products, cooking fat and anything stringy. They wrap around the impeller and are the most common reason for a pump alarm.</p>"),
    ],
    related=[
        ("blocked-drains", "Blocked drains"),
        ("leak-repairs", "Leak detection"),
        ("emergency-plumbing", "Emergency plumbing"),
        ("plumber-mount-cotton", "Plumber Mount Cotton"),
        ("plumbing-services-alberton", "Plumbing Alberton"),
        ("plumber-redland-bay", "Plumber Redland Bay"),
    ],
)
