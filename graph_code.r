# Plot for transfer portal data
library(ggplot2)
library(scales)
library(dplyr)

# Total players entering the portal, regardless of where they ended up
raw_transfer <- read.csv("Transfer_Portal_data.csv")
# Aggregate total
total_transfers <- as.data.frame(table(raw_transfer$season))
# Rename columns
colnames(total_transfers) <- c("Season", "Total")
# Graph total by year
total_transfers_plot <- ggplot(total_transfers, aes(x = Season, y = Total)) +
    geom_bar(stat = "identity", fill = "steelblue") +
    geom_text(aes(label = format(Total, big.mark = ",")), vjust = -1) +
    labs(
        title = "Total Players Entering Transfer Portal",
        x = "Season",
        y = "Total Players"
    ) +
    scale_y_continuous(labels = comma) +
    theme_classic()

# Save plot
ggsave("total_transfer_chart.jpeg", plot = total_transfers_plot, width = 8, height = 6, units = "in")
print
# Now graph player movement, first upload players and school list

players <- read.csv("transfer_22_26.csv")
players <- players[,c("season","origin","destination")]
schools <- read.csv("historical.csv")

table <- left_join(players, schools, by = c("season" = "year","origin" = "school"))

colnames(table) <- c("season","origin","destination","origin_conf","origin_type")

table <- left_join(table, schools, by = c("season" = "year", "destination" = "school"))
colnames(table) <- c("season","origin","destination","origin_conf","origin_type","destination_conf","destination_type")

table[is.na(table)] <- "lower_division"

df <- table[table$destination_conf != "lower_division" & table$origin_type != "lower_division", ]
df <- as.data.frame(table(df$season, df$origin_type, df$destination_type))
colnames(df) <- c("Season","origin","dest","count")
df$Type <- paste0(df$origin,"-",df$dest)

type_transfer_graph <- ggplot(df, aes(x = Season, y = count)) +
    geom_bar(stat = "identity", fill = "steelblue") +
    geom_text(aes(label = count), vjust = -.5) +
    facet_wrap(~Type) +
    labs(title = "Total Transfers between G6 and P4 Schools", x = "Season", y = "Total") +
    theme_classic()
ggsave("Transfer_by_type.jpeg", plot = type_transfer_graph, width = 10, height = 10, units = "in")

ld <- table[table$origin_conf == "lower_division" & table$destination_type == "g6",]
as.data.frame(table(ld$season))
