import { defineCollection, z } from "astro:content";

const blogCollection = defineCollection({
  schema: z.object({
    title: z.string(),
    pubDate: z.string().transform((str) => new Date(str)),
    excerpt: z.string(),
  }),
});

export const collections = {
  blog: blogCollection,
};
