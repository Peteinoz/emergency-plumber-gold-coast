from _common import *

page = dict(
    slug="blocked-drains-ormeau", kind="suburb", crumb="Blocked drains Ormeau",
    title="Blocked Drains Ormeau | Sewer, Storm & Septic | Moyle",
    description='Blocked drains in Ormeau and Ormeau Hills cleared from next-door Yatala: sewer, stormwater and septic lines, camera checked. Call (07) 3807 7327.',
    h1="Blocked drains Ormeau",
    eyebrow="Drains only",
    intro="<p>Blocked drains in Ormeau come in two flavours: council sewer lines in the estates and on-site septic or treatment plant drains up in Ormeau Hills and Kingsholme. Moyle Plumbing &amp; Gasfitting is based in the next suburb, carries the jetter, cable machine and camera on the van, and tells you the price before clearing starts.</p>",
    breadcrumb=[("suburbs-serviced", "Service areas")],
    service=dict(name="Blocked drain clearing in Ormeau", area="Ormeau"),
    body=sec("""
<h2>Sewered estates</h2>
<p>In the estates between the M1 and the railway line the drains are PVC and mostly under thirty years old. When they block it is nearly always what went down them: wipes, fat, sanitary items, or a child's toy. Roots turn up along the older roads and where a garden was planted over the line. Clearing is quick, and a camera check afterwards tells you whether it was a one-off or a pipe problem.</p>
<h2>Acreage on septic and treatment plants</h2>
<p>Up the hill the drains from the house go to a septic tank or a home treatment plant, then to trenches or irrigation. A "blocked drain" here can be:</p>
<ul>
<li>A blockage in the house line ahead of the tank, cleared like any other.</li>
<li>A tank that is full of solids and needs a pump-out before anything will flow.</li>
<li>A failed or blocked outlet filter on a treatment plant.</li>
<li>Saturated trenches that can no longer take the effluent, which shows as wet, smelly ground and slow drains in wet weather.</li>
<li>A dead effluent pump, which stops everything and usually sets off an alarm.</li>
</ul>
<p>We work out which before quoting, because clearing a house drain into a full tank solves nothing. Pump faults are covered under """ + L("pumps", "pumps") + """.</p>
""") + soft("""
<h2>While you wait for us</h2>
<ol class="steps">
<li>Stop putting water down the drains. Every flush and shower makes the overflow worse.</li>
<li>Find the overflow gully outside, usually a small grated pit near a bathroom wall. If it is overflowing, that is the system working as designed; keep people and pets away.</li>
<li>On septic, check whether the alarm light on the treatment plant is on and tell us.</li>
<li>Do not pour chemicals down the drain. They do not clear a real blockage and they upset a septic system.</li>
</ol>
""") + sec("""
<h2>Clearing, inspecting, fixing</h2>
<p>The machine is chosen for the cause: jetting for grease and silt, a cable for roots and solid blockages. If the line has blocked before, a camera goes down afterwards and you see what it finds. A cracked or sagging section is quoted as a separate repair, and you decide.</p>
<p>Technique and prevention tips sit on the general """ + L("blocked-drains", "blocked drains page") + """, and Coomera's estate-specific issues are on """ + L("blocked-drains-coomera", "blocked drains Coomera") + """. The rest of our Ormeau work is on the """ + L("plumber-ormeau", "Ormeau plumber page") + """. Sewage inside the house is an emergency: the """ + H("blocked sewer emergency page") + """ page has the steps. Toilets that overflow are dealt with under """ + L("toilets", "toilets") + """. Company details: """ + M("the main Moyle Plumbing site") + """.</p>
"""),
    faqs=[
        ("How can I tell my septic tank is full?",
         "<p>Slow drains throughout the house, gurgling, wet ground over the tank or trenches, and a strong smell. If it has been more than a few years since a pump-out, that is usually the answer.</p>"),
        ("Can you clear a drain on the same day in Ormeau?",
         "<p>Ormeau is next to our depot, so a blocked sewer with sewage surfacing is usually reached quickly. We tell you the realistic time when you ring.</p>"),
        ("Do tree roots mean the pipe has to be replaced?",
         "<p>Not necessarily. Roots can be cut out and the line kept clear with periodic cleaning. If the camera shows the pipe is cracked or displaced, a repair of that section is the permanent fix.</p>"),
        ("Will jetting damage old pipes?",
         "<p>Used correctly, no. We adjust pressure and nozzle to the pipe material and condition, and use the camera to check before jetting a line that may be fragile.</p>"),
    ],
    related=[
        ("blocked-drains", "Blocked drains overview"),
        ("plumber-ormeau", "Plumber Ormeau"),
        ("blocked-drains-coomera", "Blocked drains Coomera"),
        ("pumps", "Pumps"),
        ("toilets", "Toilets"),
        ("plumber-pimpama", "Plumber Pimpama"),
    ],
)
