# Startup Discovery - Customer Follow-up on Missed Calls

## Objective
Define the initial scope for a startup that helps small businesses follow up automatically after missed calls.

## Status & Progress
### Status
The concept is in early discovery. The leading approach is to detect missed calls and send an automated SMS response.

### Progress
- Identified small service businesses as the initial target.
- Drafted a missed-call-to-text workflow.
- Identified telephony and SMS as the main technical dependencies.

## Key Findings
- Missed calls are most costly when callers are high-intent and unlikely to try again.
- Small service businesses often miss calls because staff are performing the work rather than answering phones.
- SMS is a better immediate recovery channel than voicemail because it can continue asynchronously.
- The value of the product depends less on call volume than on the value of each recovered lead.

### Summary of Findings
The strongest opportunity is not businesses with the most missed calls, but businesses where a missed call can mean losing a valuable customer. That shifts discovery toward high-value service businesses and makes lead recovery, rather than general phone automation, the core product hypothesis.

## Decisions & Constraints
### Decisions
- Focus on small service businesses.
- Use SMS as the first follow-up channel.
- Keep the initial product simple.

### Constraints
- The product depends on reliable missed-call events.
- SMS delivery must meet messaging requirements.
- Phone-provider integrations may differ significantly.

## Open Questions
- Which customer segments lose the most value from missed calls?
- How often are calls missed?
- What happens after a missed call today?
- Which phone systems should be supported first?
- What pricing model would customers prefer?

## Risks & Blockers
### Blockers
- No telephony integration path has been selected.

### Risks
- Existing phone systems may already offer similar functionality.
- Integration complexity could increase quickly.
- Customers may not value the product enough to pay for it.
- SMS compliance requirements may add implementation overhead.

## Next Actions
Interview potential customers to validate the problem, then evaluate a small set of telephony providers for missed-call event support and SMS integration.

## References & Sources
- **Sources:** Telephony provider documentation, SMS provider documentation, competitor research.
- **References:** Chat history, company customer data, VoIP provider connector.
