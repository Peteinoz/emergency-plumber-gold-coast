from _common import *

page = dict(
    slug="dishwasher-installations", kind="service", crumb="Dishwasher installation",
    title="Dishwasher Installation Plumber Gold Coast | Moyle Plumbing",
    description="Dishwasher installation by a licensed plumber on the northern Gold Coast and Logan. New points, isolation taps, leak-safe connections. Call (07) 3807 7327.",
    h1="Dishwasher installation plumber",
    eyebrow="Kitchen appliances",
    intro="<p>A dishwasher installation plumber makes sure the machine you just bought does not become the reason your kitchen floor lifts. Moyle Plumbing &amp; Gasfitting installs dishwashers in homes across the northern Gold Coast, adds water and drain points where none exist, and fits the isolation tap and hoses that stop a small fault turning into a flood.</p>",
    breadcrumb=[("all-services-available", "Services")],
    service=dict(name="Dishwasher installation", area="Gold Coast"),
    body=sec("""
<h2>Two kinds of installation</h2>
<div class="two-col">
<div>
<h3>Replacing an existing dishwasher</h3>
<p>The water point, isolation tap and drain connection are already there. We disconnect and remove the old machine, check the tap and the drain spigot, fit new hoses if the old ones are tired, connect the new unit, level it, secure it to the bench and run a full cycle to check for leaks.</p>
</div>
<div>
<h3>First dishwasher in the kitchen</h3>
<p>Plenty of older houses around Beenleigh, Loganholme and Springwood were built without any dishwasher point. We run a cold water branch from the sink supply with a dedicated isolation tap, add a drain connection to the sink waste with an air gap or standpipe, and confirm a power point is within reach for your electrician.</p>
</div>
</div>
""") + soft("""
<h2>What a proper install includes</h2>
<ul class="checks">
<li>A dedicated isolation tap you can reach without pulling the machine out.</li>
<li>Braided inlet hose rated for the pressure, with a check that the mains pressure is within the appliance's limit.</li>
<li>Drain hose looped high or connected to a proper spigot so sink water cannot siphon back into the machine.</li>
<li>Machine levelled and fixed so the door does not tip it forward.</li>
<li>A test cycle with the plumber present, checking every connection while under pressure and during the drain.</li>
<li>Old appliance removed if you want it gone.</li>
</ul>
<p>Many Gold Coast estates have high mains pressure. If yours is above the appliance rating, a pressure limiting valve protects the dishwasher, the washing machine and every flexible hose in the house.</p>
""") + sec("""
<h2>Integrated and drawer dishwashers</h2>
<p>Fully integrated machines behind a cabinet door and double-drawer units need the water and drain points in precise positions, usually in the adjacent cabinet rather than behind the machine. If you are renovating, get us in before the cabinetry is fixed so the points land where the appliance manual wants them. It is a small visit that avoids cutting cabinets later.</p>
<h2>Dishwasher leaks: what we see</h2>
<p>Most dishwasher floods on the northern Gold Coast come from a split inlet hose, a drain hose pushed loosely into the waste, or a machine that was never levelled and has been rocking against its connections. If you find water under the machine, close the isolation tap first, then the meter if there is no tap, and ring us. A running leak is handled the same way as any other on the """ + H("kitchen flood emergency page") + """.</p>
<p>The same visit can cover an """ + L("insinkerator", "InSinkErator waste disposer") + """, a """ + L("water-filter-installation", "filtered water tap") + """ or a new mixer, all part of the """ + L("general-plumbing-maintenance", "everyday plumbing") + """ we do around kitchens. Leak tracing under benches is described on the """ + L("leak-repairs", "leak repairs page") + """. The company's background is on the """ + M("Moyle Plumbing website") + """.</p>
""") + sec("""
<h2>Rental properties and new dishwashers</h2>
<p>Property managers often have a tenant asking whether they can install their own dishwasher. The answer depends on whether a point exists. Where it does, the tenant's machine connects to the existing tap and drain and the owner's plumbing is untouched. Where it does not, adding a point changes the owner's plumbing and needs the owner's approval and a licensed plumber; we do those installs against a work order and photograph the finished connection for the file. At the end of the tenancy we can disconnect and cap the point so the next tenant's machine can be connected cleanly.</p>
"""),
    faqs=[
        ("Do I need a plumber or can the retailer install it?",
         "<p>A like-for-like swap onto an existing tap and drain is often done by delivery crews. Any new water or drain connection, or a change to the pipework under the sink, is licensed plumbing work in Queensland.</p>"),
        ("Does the dishwasher need hot or cold water?",
         "<p>Most modern dishwashers heat their own water and connect to cold. Some can take hot. We check the manual and connect it the way the manufacturer specifies.</p>"),
        ("Can you install a dishwasher on the same day as delivery?",
         "<p>Usually, if the machine is on site and the point exists. For a first-time installation we may need to see the kitchen first to work out the pipe route.</p>"),
        ("Why does my sink fill when the dishwasher drains?",
         "<p>The drain is restricted, usually by grease in the sink waste. The dishwasher pump pushes water faster than the partly blocked pipe can take it. Clearing the waste fixes it.</p>"),
    ],
    related=[
        ("insinkerator", "InSinkErator installation"),
        ("water-filter-installation", "Water filter installation"),
        ("general-plumbing-maintenance", "Plumbing maintenance"),
        ("leak-repairs", "Leak repairs"),
        ("plumber-hope-island", "Plumber Hope Island"),
        ("plumber-coomera", "Plumber Coomera"),
    ],
)
