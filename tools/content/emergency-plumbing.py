from _common import *

page = dict(
    slug="emergency-plumbing", kind="service", crumb="Emergency plumbing",
    title="Emergency Plumbing Services Gold Coast | Moyle Plumbing",
    description="Urgent plumbing across the northern Gold Coast, Beenleigh and Logan from Yatala-based licensed plumbers. Set price before work starts. Call (07) 3807 7327.",
    h1="Emergency plumbing services, northern Gold Coast",
    eyebrow="Urgent callouts",
    intro="<p>Emergency plumbing services from Moyle Plumbing &amp; Gasfitting cover the faults that cannot wait: burst pipes, sewer backing up, gas smells, failed hot water and leaks through ceilings. This page explains what counts, what we do when we arrive, and how the callout is priced so you are not guessing.</p>",
    breadcrumb=[("all-services-available", "Services")],
    service=dict(name="Emergency plumbing services", area="Gold Coast", description="Urgent plumbing and gas callouts across the northern Gold Coast, Beenleigh, Logan and Brisbane's southside."),
    body=sec("""
<h2>What counts as a plumbing emergency</h2>
<p>A fair test is damage or safety. If leaving the fault overnight would damage the building, make someone sick or put anyone at risk, it is an emergency. Everything else is important, but it can be booked.</p>
<table>
<thead><tr><th>Treat as urgent</th><th>Book a normal visit</th></tr></thead>
<tbody>
<tr><td>Water flowing that you cannot isolate</td><td>Dripping tap or shower head</td></tr>
<tr><td>Sewage rising at a gully, shower or toilet</td><td>One slow basin or bath</td></tr>
<tr><td>Gas smell, hissing or a yellow lazy flame</td><td>Gas cooktop igniter clicking but lighting normally</td></tr>
<tr><td>Hot water tank leaking from the cylinder</td><td>Relief valve dripping a little while heating</td></tr>
<tr><td>Ceiling bulging or dripping</td><td>Small stain that is dry to touch</td></tr>
<tr><td>Only toilet in the home out of action</td><td>Cistern slow to refill</td></tr>
</tbody>
</table>
<p>Not sure? Ring """ + PHONE + """ and describe it. We would rather talk you through a quick isolation than have you wait with water running.</p>
""") + soft("""
<h2>How an urgent callout runs</h2>
<ol class="steps">
<li><strong>The call.</strong> Tell us the suburb, what is happening and whether you have managed to shut anything off. If there is a gas smell we will tell you to isolate at the meter and get outside before anything else.</li>
<li><strong>Dispatch.</strong> We confirm who is coming from Yatala and give you a realistic window. Where the emergency is real, attendance that day is the target, and we never quote an arrival we cannot honour.</li>
<li><strong>Diagnosis on site.</strong> The plumber shuts the fault down, assesses the damage and settles on a lasting fix rather than a patch.</li>
<li><strong>Set price.</strong> The repair cost is confirmed with you before anything begins. Should a wall or trench reveal more, that extra is discussed and agreed first.</li>
<li><strong>Repair and test.</strong> Water repairs get a pressure test. Gas repairs get a leak test across the installation. Drains are run and checked with a camera where the cause is not obvious.</li>
<li><strong>Clean up.</strong> We tidy up, and you are told what to watch for.</li>
</ol>
""") + sec("""
<h2>The urgent jobs we attend most</h2>
""" + cards([
    ("burst-pipe", "Burst pipe repair", "Split copper, cracked poly, failed flexi hoses and joints that have parted. Shut off, replace the section, test."),
    ("blocked-drains", "Blocked drains and sewer", "Main line blockages that stop every drain in the house, cleared with jetting or a machine cable and inspected with a camera."),
    ("hot-water", "No hot water", "Tripped elements, failed thermostats, leaking cylinders and units that have simply reached the end. Repair or replace, decided with you."),
    ("gas-fitting", "Gas leaks", "Licensed gasfitters find the leak, repair it and pressure test the whole installation before restoring supply."),
    ("leak-repairs", "Leaks through walls and ceilings", "Water showing up where it should not, traced back to the source rather than just dried out."),
    ("toilets", "Toilet failures", "Overflowing pans, blocked outlets and cisterns that will not stop running."),
]) + """
<p>If you are on this page from a search for an urgent plumber, the """ + H("emergency plumber Gold Coast home page") + """ runs through what to shut off first: water meter, gas meter and the hot water circuit.</p>
<h2>Where we cover from Yatala</h2>
<p>Yatala is positioned at the junction of the northern Gold Coast, Beenleigh and Logan, so the reach is wide. The suburbs we most often attend for urgent work are """ + L("plumber-coomera", "Coomera") + """, Pimpama and Ormeau, then Hope Island, """ + L("emergency-plumbers-helensvale", "Helensvale") + """, """ + L("emergency-plumber-beenleigh", "Beenleigh") + """, Loganholme and Shailer Park, and further out to the southside and the Redlands.</p>
<h2>Safety first, always</h2>
""" + callout("""<p><strong>Gas:</strong> never hunt for or attempt to fix a gas leak. Close the valve at the meter or cylinder, open the house up, leave switches alone and phone from outside.</p>
<p><strong>Electricity:</strong> if water is near power points, the switchboard or the hot water unit, switch the circuit off at the board before doing anything else. If the board itself is wet, stay away from it and call an electrician as well.</p>
<p><strong>Sewage:</strong> keep the family and pets out of affected areas until it is cleared and disinfected.</p>""", warn=True) + """
<p>Moyle Plumbing &amp; Gasfitting, a family concern since 1983, is licensed and insured across plumbing and gas. Further background is on the """ + M("Moyle Plumbing &amp; Gasfitting") + """ main site.</p>
"""),
    faqs=[
        ("Can I get an emergency plumber out today?",
         "<p>On genuine emergencies we aim for same-day attendance across the northern Gold Coast, Beenleigh and Logan. Ring us, describe the fault and we will tell you honestly what the day looks like.</p>"),
        ("Will the price be higher because it is urgent?",
         "<p>Callout charges are explained before dispatch. Once on site, the repair itself is quoted as a fixed figure and you are free to decline.</p>"),
        ("What if the leak is inside a wall or under the slab?",
         "<p>We isolate the water first so the damage stops, then use leak detection equipment to pinpoint the fault before opening anything. That keeps the repair small and the mess down.</p>"),
        ("Do you handle both plumbing and gas emergencies?",
         "<p>Yes. Holding plumbing and gas licences together means a gas leak, a hot water failure or a burst pipe can all be handled by the same tradesperson.</p>"),
    ],
    related=[
        ("burst-pipe", "Burst pipe repair"),
        ("blocked-drains", "Blocked drains"),
        ("hot-water", "Hot water repairs"),
        ("gas-fitting", "Gas fitting"),
        ("leak-repairs", "Leak detection"),
        ("emergency-plumber-beenleigh", "Emergency plumber Beenleigh"),
        ("emergency-plumbers-helensvale", "Emergency plumbers Helensvale"),
        ("plumber-coomera", "Plumber Coomera"),
    ],
)
