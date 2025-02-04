import publicWidget from "@web/legacy/js/public/public_widget";
import { rpc } from "@web/core/network/rpc";

publicWidget.registry.DynamicAppeals = publicWidget.Widget.extend({
    selector: '#explore-appeals',

    start() {
        console.log("DynamicAppeals Widget Initialized");
        this._fetchAndRenderAppeals();
        return this._super.apply(this, arguments);
    },

    async _fetchAndRenderAppeals() {
        const appealsCarousel = document.getElementById('dynamic-appeals-carousel');
        console.log("Appeals Carousel:", appealsCarousel);

        if (!appealsCarousel) {
            console.error("Element #dynamic-appeals-carousel not found");
            return;
        }

        appealsCarousel.innerHTML = '<div class="text-center">Loading appeals...</div>';

        try {
            const data = await rpc("/appeals/", { params: {} });

            console.log('Appeals fetched successfully:', data);

            if (data.length === 0) {
                appealsCarousel.innerHTML = '<div class="text-center">No appeals available.</div>';
                return;
            }

            appealsCarousel.innerHTML = data.map((appeal, index) => {
                const isActive = index === 0 ? "active" : "";
                return `
                    <div class="carousel-item ${isActive}">
                        <div class="appeal my-2 shadow-sm">
                            <div class="container text-white" style="background-color:black;">
                                <div class="row">
                                    <div class="col-md-6">
                                        <img class="img-fluid rounded" src="data:image/png;base64,${appeal.banner_image}" alt="${appeal.name}" />
                                        <div class="d-flex align-items-center my-3" style="padding: 0px 15px;">
                                            <span>Raised <b>${appeal.total_contribution}</b></span>
                                            <div class="progress mx-3" style="flex-grow: 1;">
                                                <div class="progress-bar" role="progressbar" style="width: ${calculateProgress(appeal.total_contribution, appeal.goal)}%" aria-valuenow="${calculateProgress(appeal.total_contribution, appeal.goal)}" aria-valuemin="0" aria-valuemax="100">
                                                    ${calculateProgress(appeal.total_contribution, appeal.goal)}%
                                                </div>
                                            </div>
                                            <span>Goal <b>${appeal.goal}</b></span>
                                        </div>
                                    </div>
                                    <div class="col-md-6">
                                        <h2 class="card-title mt-2">${appeal.name}</h2>
                                        <hr>
                                        <h4 class="card-title">Goal: ${appeal.goal}</h4>
                                        <p class="card-text">Start Date: ${appeal.start_date}</p>
                                        <p class="card-text">End Date: ${appeal.end_date}</p>
                                        <p class="card-text">Collected Amount: ${appeal.total_contribution}</p>
                                        <p class="card-text">Supporters: ${appeal.total_partners}</p>
                                        <p class="mt-2" style="background-color: red; display: inline; padding: 10px; border-radius: 11px;">
                                            <a class="text-white" href="/donation/pay/appeals/${appeal.id}">Donate Now</a>
                                        </p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                `;
            }).join('');
        } catch (error) {
            console.error('Error fetching appeals:', error);
            appealsCarousel.innerHTML = '<div class="text-center text-danger">Error loading appeals.</div>';
        }
    },
});

function calculateProgress(totalContribution, goal) {
    if (goal <= 0) return 0;
    return Math.min((totalContribution / goal) * 100, 100);
}

export default publicWidget.registry.DynamicAppeals;
