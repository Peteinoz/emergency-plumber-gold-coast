from _common import *

page = dict(
    slug="insinkerator", kind="service", crumb="InSinkErator",
    title="InSinkErator Installation Gold Coast | Moyle Plumbing",
    description='InSinkErator installation and replacement by licensed plumbers on the northern Gold Coast and Logan, drains connected right. Call (07) 3807 7327.',
    h1="InSinkErator installation and replacement",
    eyebrow="Waste disposers",
    intro="<p>An InSinkErator installation is straightforward when the sink, drain and power point are ready for it, and a mess when they are not. Moyle Plumbing &amp; Gasfitting fits new food waste disposers and replaces worn ones in homes from the northern Gold Coast to Logan, connecting the drain and dishwasher correctly so the unit does not flood the cupboard.</p>",
    breadcrumb=[("all-services-available", "Services")],
    service=dict(name="InSinkErator installation", area="Gold Coast"),
    body=sec("""
<h2>Before you buy one</h2>
<ul class="checks">
<li><strong>Sink outlet.</strong> Disposers need a standard 90 mm sink hole. Older sinks with small outlets need a new bowl or an adaptor, and some granite composite sinks need care with the mounting.</li>
<li><strong>Space under the bench.</strong> The unit hangs below the sink and needs clearance for the drain elbow and the dishwasher connection.</li>
<li><strong>Power.</strong> A switched power point under the sink, and either an air switch on the bench or a wall switch. Your electrician does that part; we coordinate.</li>
<li><strong>Drain.</strong> The sink waste has to be in good condition and free of grease. A disposer into a half-blocked pipe blocks it fully.</li>
<li><strong>Septic or treatment plant?</strong> Ground-up food changes the load on an on-site system. On acreage we advise before installing.</li>
</ul>
""") + soft("""
<h2>What we do on the day</h2>
<ol class="steps">
<li>Remove the existing basket waste or old disposer and clean the sink flange area.</li>
<li>Fit the new mounting assembly with the correct seal so the sink does not leak around the flange.</li>
<li>Hang the unit, connect the drain elbow with a proper trap and the dishwasher inlet if you have one.</li>
<li>Check the power connection is in place, then run water and test with the unit on and off.</li>
<li>Show you what it will and will not handle.</li>
</ol>
<p>A replacement of the same brand usually reuses the mounting, which makes the swap quick. A first-time install includes drilling for an air switch if you choose one.</p>
""") + sec("""
<h2>Living with a disposer</h2>
<p>Run cold water before, during and after use so fat stays solid enough to pass through. Feed it gradually. Keep out fibrous vegetables such as celery and corn husks, large bones, coffee grounds in quantity, and anything that is not food. If it hums but will not turn, switch it off, use the hex key in the base to free the plate and press the reset button underneath. If it trips repeatedly or leaks from the body, the motor or seals have gone and replacement is the usual answer.</p>
<p>Disposers and dishwashers share a drain, so a """ + L("dishwasher-installations", "dishwasher installation") + """ is often done at the same time, along with a """ + L("water-filter-installation", "filtered water tap") + """. A kitchen sink that backs up after a disposer has been running is a job for the """ + L("blocked-drains", "blocked drains page") + """. If the cupboard is full of water, close the tap under the sink and follow the """ + H("urgent kitchen plumbing page") + """ steps. We fit disposers in """ + L("plumber-hope-island", "Hope Island") + """, """ + L("plumber-coomera", "Coomera") + """ and across the northern Gold Coast; for the wider business see """ + M("the company's main website") + """.</p>
""") + sec("""
<h2>Which model?</h2>
<p>Disposers differ mainly in motor size, grinding stages and noise. A small household with light use is well served by an entry model; a big family kitchen that puts a lot through it benefits from a stronger motor and finer grinding, which also handles the occasional bone without jamming. Quieter models cost more and are worth it in open-plan homes where the kitchen is the living room. Whatever you choose, look for a unit with a replaceable splash guard and a reset button you can reach, because both get used. Tell us how the kitchen is used and we will suggest a size rather than the biggest one on the shelf.</p>
"""),
    faqs=[
        ("Can an InSinkErator be fitted to any sink?",
         "<p>Most modern stainless and composite sinks with a standard outlet take one. Very old or small-outlet sinks may need a new bowl. We check the sink before quoting.</p>"),
        ("Does it need its own power point?",
         "<p>It needs a power point under the sink and a means of switching it. An electrician installs those; we install the disposer and make the plumbing connections.</p>"),
        ("Why does my disposer leak underneath?",
         "<p>Leaks at the top are the sink flange seal; at the side, the drain or dishwasher connection; from the bottom of the body, a failed internal seal, which means the unit is done.</p>"),
        ("Will it block my drains?",
         "<p>Not if the drain was clear to begin with and it is used with plenty of cold water. Grease already in the line is the usual cause of a blockage after a disposer goes in.</p>"),
    ],
    related=[
        ("dishwasher-installations", "Dishwasher installation"),
        ("blocked-drains", "Blocked drains"),
        ("water-filter-installation", "Water filter installation"),
        ("plumber-hope-island", "Plumber Hope Island"),
        ("plumber-coomera", "Plumber Coomera"),
    ],
)
