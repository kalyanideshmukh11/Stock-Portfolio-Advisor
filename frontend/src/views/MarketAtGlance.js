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
                    "title": "Indices",
                    "symbols": [
                        {
                            "s": "OANDA:SPX500USD",
                            "d": "S&P 500"
                        },
                        {
                            "s": "INDEX:XLY0",
                            "d": "Shanghai Composite"
                        },
                        {
                            "s": "FOREXCOM:DJI",
                            "d": "Dow 30"
                        },
                        {
                            "s": "INDEX:NKY",
                            "d": "Nikkei 225"
                        },
                        {
                            "s": "INDEX:DAX",
                            "d": "DAX Index"
                        },
                        {
                            "s": "CURRENCYCOM:US100",
                            "d": "NASDAQ 100"
                        },
                        {
                            "s": "BSE:SENSEX",
                            "d": "S&P BSE SENSEX INDEX"
                        }
                    ],
                    "originalTitle": "Indices"
                },
                {
                    "title": "Commodities",
                    "symbols": [
                        {
                            "s": "CME_MINI:ES1!",
                            "d": "E-Mini S&P"
                        },
                        {
                            "s": "CME:E61!",
                            "d": "Euro"
                        },
                        {
                            "s": "COMEX:GC1!",
                            "d": "Gold"
                        },
                        {
                            "s": "NYMEX:CL1!",
                            "d": "Crude Oil"
                        },
                        {
                            "s": "NYMEX:NG1!",
                            "d": "Natural Gas"
                        },
                        {
                            "s": "CBOT:ZC1!",
                            "d": "Corn"
                        }
                    ],
                    "originalTitle": "Commodities"
                },
                {
                    "title": "Bonds",
                    "symbols": [
                        {
                            "s": "CME:GE1!",
                            "d": "Eurodollar"
                        },
                        {
                            "s": "CBOT:ZB1!",
                            "d": "T-Bond"
                        },
                        {
                            "s": "CBOT:UD1!",
                            "d": "Ultra T-Bond"
                        },
                        {
                            "s": "EUREX:GG1!",
                            "d": "Euro Bund"
                        },
                        {
                            "s": "EUREX:II1!",
                            "d": "Euro BTP"
                        },
                        {
                            "s": "EUREX:HR1!",
                            "d": "Euro BOBL"
                        }
                    ],
                    "originalTitle": "Bonds"
                },
                {
                    "title": "Forex",
                    "symbols": [
                        {
                            "s": "FX:EURUSD"
                        },
                        {
                            "s": "FX:GBPUSD"
                        },
                        {
                            "s": "FX:USDJPY"
                        },
                        {
                            "s": "FX:USDCHF"
                        },
                        {
                            "s": "FX:AUDUSD"
                        },
                        {
                            "s": "FX:USDCAD"
                        }
                    ],
                    "originalTitle": "Forex"
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