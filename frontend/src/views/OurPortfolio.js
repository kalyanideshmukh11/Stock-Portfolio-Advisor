import React from 'react'
export default class MarketAtGlance extends React.Component {
    componentDidMount() {
        const script = document.createElement('script');
        script.src = 'https://s3.tradingview.com/external-embedding/embed-widget-market-overview.js'
        script.async = true;
        script.innerHTML = JSON.stringify({
            "showChart": true,
            "locale": "en",
            "largeChartUrl": "",
            "width": "100%",
            "height": "660",
            "plotLineColorGrowing": "rgba(33, 150, 243, 1)",
            "plotLineColorFalling": "rgba(33, 150, 243, 1)",
            "gridLineColor": "rgba(233, 233, 234, 1)",
            "scaleFontColor": "rgba(131, 136, 141, 1)",
            "belowLineFillColorGrowing": "rgba(5, 122, 205, 0.12)",
            "belowLineFillColorFalling": "rgba(5, 122, 205, 0.12)",
            "symbolActiveColor": "rgba(225, 239, 249, 1)",
            "tabs": [
                {
                    "title": "Our Portfolio",
                    "symbols": [
                        {
                            "s": "NASDAQ:AAPL",
                            "d": "APPLE INC"
                        },
                        {
                            "s": "NASDAQ:TSLA",
                            "d": "TESLA INC"
                        },
                        {
                            "s": "NASDAQ:ADBE",
                            "d": "ADOBE INC"
                        },
                        {
                            "s": "NASDAQ:AMZN",
                            "d": "AMAZON COM INC"
                        },
                        {
                            "s": "NYSE:VEEV",
                            "d": "VEEVA SYSTEMS INC"
                        },
                        {
                            "s": "NYSE:NOW",
                            "d": "SERVICENOW INC"
                        },
                        {
                            "s": "NASDAQ:NVDA",
                            "d": "NVIDIA CORP"
                        },
                        {
                            "s": "NASDAQ:GOOGL",
                            "d": "ALPHABET INC (GOOGLE) CLASS A"
                        },
                        {
                            "s": "NASDAQ:CSCO",
                            "d": "CISCO SYSTEMS INC"
                        },
                        {
                            "s": "NASDAQ:INTC",
                            "d": "INTEL CORP"
                        },
                        {
                            "s": "NYSE:T",
                            "d": "AT&T INC"
                        },
                        {
                            "s": "NYSE:CVS",
                            "d": "CVS HEALTH CORPORATION"
                        }
                    ],
                    "originalTitle": "Our Portfolio"
                }
            ]
        });
        document.getElementById("data").appendChild(script);
    }
    render() {
        return (
            <div>
                <div className="box effect1" style={{ textAlign: 'center' }}>
                    <div id="data">
                        <div className="tradingview-widget-container">
                            <div className="tradingview-widget-container__widget"></div>

                        </div>
                    </div>
                    <br/><br/>
                </div>
            </div>
        )
    }
}