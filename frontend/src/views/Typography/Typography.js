import React from "react";
// @material-ui/core components
import { makeStyles } from "@material-ui/core/styles";
// core components
import Card from "components/Card/Card.js";
import CardHeader from "components/Card/CardHeader.js";
import CardBody from "components/Card/CardBody.js";

const styles = {
  typo: {
    paddingLeft: "25%",
    marginBottom: "40px",
    position: "relative"
  },
  note: {
    fontFamily: '"Roboto", "Helvetica", "Arial", sans-serif',
    bottom: "10px",
    color: "#c0c1c2",
    display: "block",
    fontWeight: "400",
    fontSize: "13px",
    lineHeight: "13px",
    left: "0",
    marginLeft: "20px",
    position: "absolute",
    width: "260px"
  },
  cardCategoryWhite: {
    color: "rgba(255,255,255,.62)",
    margin: "0",
    fontSize: "14px",
    marginTop: "0",
    marginBottom: "0"
  },
  cardTitleWhite: {
    color: "#FFFFFF",
    marginTop: "0px",
    minHeight: "auto",
    fontWeight: "300",
    fontFamily: "'Roboto', 'Helvetica', 'Arial', sans-serif",
    marginBottom: "3px",
    textDecoration: "none"
  }
};

const useStyles = makeStyles(styles);

export default function TypographyPage() {
  const classes = useStyles();
  return (
    <Card>
      <CardHeader color="warning">
        <h4 className={classes.cardTitleWhite}>Investment Strategies</h4>
        <p className={classes.cardCategoryWhite}>
          Find details about all the investment strategies
        </p>
      </CardHeader>
      <CardBody>
        <h3>Ethical Investing</h3>
        <p>Ethical investing refers to the practice of using one's ethical principles as the primary filter for the selection of securities investing. Ethical investing depends on the investor's views. Ethical investing is sometimes used interchangeably with socially conscious investing; however, socially conscious funds typically have one overarching set of guidelines that are used to select the portfolio, whereas ethical investing brings about a more personalized result.</p>

        <h3>Growth Investing</h3>
        <p>Growth investing is an investment style and strategy that is focused on increasing an investor's capital. Growth investors typically invest in growth stocks—that is, young or small companies whose earnings are expected to increase at an above-average rate compared to their industry sector or the overall market.

        Growth investing is highly attractive to many investors because buying stock in emerging companies can provide impressive returns if the companies are successful. However, such companies are untried, and thus often pose a fairly high risk.</p>

        <h3>Index Investing</h3>
        <p>Index investing is a passive investment strategy that attempts to generate returns similar to a broad market index. Investors use this buy-and-hold strategy to replicate the performance of a specific index – generally an equity or fixed-income index – by purchasing the component securities of the index, or else an index mutual fund or exchange-traded funds (ETF) that itself closely tracks the underlying index.</p>

        <h3>Quality Investing</h3>
        <p>Factor investing is a strategy that chooses securities on attributes that are associated with higher returns. There are two main types of factors that have driven returns of stocks, bonds, and other factors: macroeconomic factors and style factors. The former captures broad risks across asset classes while the latter aims to explain returns and risks within asset classes.</p>

        <h3>Value Investing</h3>
        <p>Value investing is an investment strategy that involves picking stocks that appear to be trading for less than their intrinsic or book value. Value investors actively ferret out stocks they think the stock market is underestimating. They believe the market overreacts to good and bad news, resulting in stock price movements that do not correspond to a company's long-term fundamentals. The overreaction offers an opportunity to profit by buying stocks at discounted prices—on sale.</p>

      </CardBody>
    </Card>
  );
}
